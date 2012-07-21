# -*-*- encoding: utf-8 -*-*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('ira.views',
    url(r'^$', 'ira'),
)
