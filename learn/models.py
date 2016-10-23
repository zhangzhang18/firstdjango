# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import ast


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self.name


# python manage.py makemigrations
# python manage.py migrate

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class RemarkForm(forms.Form):
        TOPIC_CHOICES = (
        ('leve1', '差评'),
        ('leve2', '中评'),
        ('leve3', '好评'),
        )
        subject = forms.CharField(max_length=100 ,label='留言标题')
        mail = forms.EmailField(label='电子邮件')
        topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
        message = forms.CharField(label='留言内容',widget=forms.Textarea)
        cc_myself = forms.BooleanField(required=False ,label='订阅该贴')
