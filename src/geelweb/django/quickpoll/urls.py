# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from django.conf.urls.defaults import patterns, url
from geelweb.django.quickpoll.views import PollRestView, PollRulesRestView, PollTemplateView

urlpatterns = patterns('',
    url(r'^rest/poll/(?P<poll_id>\d+)$', PollRestView.as_view()),
    url(r'^rest/poll/(?P<poll_id>\d+)/rules$', PollRulesRestView.as_view()),

    url(r'^templates/poll/(?P<poll_id>\d+)$', PollTemplateView.as_view()),
)
