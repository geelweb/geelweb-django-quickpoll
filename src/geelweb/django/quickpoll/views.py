# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from geelweb.django.quickpoll.models import Poll, Question, Rule
from geelweb.django.quickpoll.serializers import PollSerializer, RuleSerializer

from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class PollRestView(View):
    """
    A view to manage get/post queries on quickpoll/rest/poll/<id>
    """

    def get(self, request, *args, **kwargs):
        """
        Gets the json representation of the poll
        """
        poll = get_object_or_404(Poll, pk=kwargs['poll_id'])
        return JSONResponse(PollSerializer(poll).data)

    def post(self, request, *args, **kwargs):
        """
        Saves the polls votes
        """
        poll = get_object_or_404(Poll, pk=kwargs['poll_id'])
        questions = poll.question_set.all();

        for question in questions:
            key = 'choice_%d' % question.id
            if key in request.POST:
                selected_choice = question.choice_set.get(pk=request.POST[key])
                selected_choice.votes += 1
                selected_choice.save()

        return JSONResponse({
            'state': 'ok',
            'poll_id': poll.id})


class PollRulesRestView(View):
    """
    A view to manage get queries on quickpoll/rest/poll/<id>/rules
    """

    def get(self, request, *args, **kwargs):
        """
        Gets the poll rules
        """
        poll = get_object_or_404(Poll, pk=kwargs['poll_id'])
        rules = Rule.objects.filter(poll=poll)
        collection = []
        for rule in rules:
            collection.append(RuleSerializer(rule).data)
        return JSONResponse(collection)


class PollTemplateView(View):
    """
    A view to manage get queries on quickpoll/templates/poll/<id>
    """

    def get(self, request, *args, **kwargs):
        """
        Renders the poll dialog form
        """
        poll = get_object_or_404(Poll, pk=kwargs['poll_id'])
        questions = Question.objects.filter(poll=poll)
        return render_to_response('quickpoll/poll_template.html', {
            'poll': poll,
            'questions': questions,
            },
            context_instance=RequestContext(request))
