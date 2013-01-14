# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:
#
# pylint: disable=E1101
# pylint: disable=W0232
# pylint: disable=R0903

"""
Quickpoll application models
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from django.db import models

class Poll(models.Model):
    """
    Poll model
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Question(models.Model):
    """
    Question model
    """
    poll = models.ForeignKey(Poll)
    rank = models.IntegerField(default=0)
    question = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        """
        Meta class
        """
        ordering = ['rank']

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    """
    Question choice model
    """
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    class Meta:
        """
        Meta class
        """
        ordering = ['rank']

    def __unicode__(self):
        return self.choice

class Rule(models.Model):
    """
    Poll rule model
    """
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    choices = models.ManyToManyField(Choice)
    questions_displayed = models.ManyToManyField(
            Question,
            related_name="%(app_label)s_%(class)s_related")

    def __unicode__(self):
        return '%s - %s' % (self.poll.title, self.question.question)

