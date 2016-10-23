# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # 会自动做一些处理去适应python不同的版本
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateField(u'更新时间', auto_now_add=True, editable=True)

    # def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
    #     return self.title
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):  # str_on python 3
        return self.name

