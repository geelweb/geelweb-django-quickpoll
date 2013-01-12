# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from rest_framework import serializers
from geelweb.django.quickpoll.models import Poll, Question, Rule

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
