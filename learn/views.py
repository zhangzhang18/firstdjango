#!usr/bin/python
# -*-coding:utf-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
import os
import json


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


def index(request):
    info_dict = {'site': u'张', 'content': u'python技术教程'}
    return render(request, 'home.html', {'info_dict': info_dict})


def home(request):
    return render(request, 'base.html', )


def ajax(request):
    return render(request, 'ajaxindex.html', )


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def my_view(request):
    context = {'some_key': 'some_value'}
    static_html = 'static/static.html'
    if not os.path.exists(static_html):
        content = render_to_string('template.html', context)
        with open(static_html, 'w') as static_file:
            static_file.write(content)
    return render_to_string(request, static_html)
