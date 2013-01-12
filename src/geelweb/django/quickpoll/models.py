# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class Question(models.Model):
    poll = models.ForeignKey(Poll)
    rank = models.IntegerField()
    question = models.CharField(max_length=200)

    class Meta:
        ordering = ['rank']

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=200)
    rank = models.IntegerField()
    votes = models.IntegerField()

    class Meta:
        ordering = ['rank']

    def __unicode__(self):
        return self.choice

class Rule(models.Model):
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    choices = models.ManyToManyField(Choice)
    questions_displayed = models.ManyToManyField(Question, related_name="%(app_label)s_%(class)s_related")

    def __unicode__(self):
        return '%s - %s' % (self.poll.title, self.question.question)

