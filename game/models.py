from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
# Create your models here.
# @python_2_unicode_compatible
# class User(models.Model):
#     name = models.CharField(max_length=64)
#     password = models.CharField(max_length=32)
#     def __str__(self):
#         return self.name

@python_2_unicode_compatible
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default = 1)
    def __str__(self):
        to_string = self.user.username + str(self.points)
