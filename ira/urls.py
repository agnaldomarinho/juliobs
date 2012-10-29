# -*-*- encoding: utf-8 -*-*-
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from views import *

urlpatterns = patterns('ira.views',
    url(r'^$', TemplateView.as_view(template_name='ira/index.html'), name="index"),
    url(r'^login/$', login, name="login"),
    url(r'^historico/$', enfase, name="enfase"),
    url(r'^prever/$', prever, name="prever"),
    url(r'^html_up/$', html_upload, name="html_upload"),
)
