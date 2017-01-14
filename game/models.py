from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone


@python_2_unicode_compatible
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default = 1)
    def __str__(self):
        to_string = self.user.username + str(self.points)
        return to_string
#
# @python_2_unicode_compatible
# class Student(models.Model):
#     user = models.OneToOneField(User)
#

@python_2_unicode_compatible
class Scenarios(models.Model):
    notes = models.TextField()
    creator = models.CharField(max_length = 512)
    active = models.BooleanField(default = False)
    name = models.CharField(max_length = 512, default = str(timezone.now()))
    num_lives = models.IntegerField(default = 1);
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Scenario_Completed_By(models.Model):
    scenario = models.ForeignKey(Scenarios)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.user.username + " completed "+ self.scenario.name

@python_2_unicode_compatible
class Badge(models.Model):
    condition_choices = (
        ('1', 'Points'),
        ('2', 'Scenario'),
    )
    badge_type = models.CharField(max_length = 2, choices = condition_choices)
    points = models.IntegerField(default = 0)
    scenario = models.ForeignKey(Scenarios)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.user.username + " " + self.scenario.name + " " + str(self.points)
