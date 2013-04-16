# -*-*- encoding: utf-8 -*-*-
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from views import *

urlpatterns = patterns('cg_t4.views',
    url(r'^$', TemplateView.as_view(template_name='cg_t4/index.html'), name="index"),
    url(r'^mario/$', TemplateView.as_view(template_name='cg_t4/mario.html'), name="mario"),
)
