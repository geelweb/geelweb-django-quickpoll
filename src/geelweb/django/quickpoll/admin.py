# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
quickpoll admin
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from django.contrib import admin
from geelweb.django.quickpoll.models import Poll, Question, Choice, Rule

class ChoiceInline(admin.TabularInline):
    """
    Choice inline
    """
    model = Choice
    extra = 3
    fieldsets = [
            (None, {'fields': ['choice', 'rank']})
            ]

class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin
    """
    fieldsets = [
            (None, {'fields': ['question', 'poll', 'rank']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'rank', 'poll')

admin.site.register(Poll)
admin.site.register(Rule)
admin.site.register(Question, QuestionAdmin)

