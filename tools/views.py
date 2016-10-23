# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .form import ADDForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 引入我们创建的表单类
def index2(request):
    if request.method == 'POST':  # 当提交表单时

        form = ADDForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = ADDForm()
    return render(request, 'index.html', {'form': form, })
