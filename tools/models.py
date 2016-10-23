# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
