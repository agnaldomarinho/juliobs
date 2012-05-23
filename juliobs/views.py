#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-

"""
Meus views
"""
__author__ = "Julio Batista Silva"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"

from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    return render_to_response('homepage.html', locals(),
            context_instance=RequestContext(request))
