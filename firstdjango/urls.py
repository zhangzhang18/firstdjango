"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auto_urls
from learn import views as learn_views  # new
from tools import views as tools_views
from blog import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^blogindex/$', blog_views.index, name='blogindex'),
    url(r'^get_pic/$', blog_views.get_pic, name='get-pic'),
    url(r'ajax/$', learn_views.ajax, name='ajaxindex'),
    url(r'^ajax_list/$', learn_views.ajax_list, name='ajax_liat'),
    url(r'^ajax_dict/$', learn_views.ajax_dict, name='ajax_dict'),
    url(r'^form/$', tools_views.index2, name='index'),
    url(r'^add/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^html/$', learn_views.my_view, name='my_view'),
    url(r'^add/$', learn_views.add, name='add'),
    url(r'home/$', learn_views.home, name='home'),
    url(r'^$', learn_views.index, name='index'),  # new
    #  python manage.py runserver
    url(r'^accounts/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
