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
from django.http import HttpResponse


def homepage(request):
    return render_to_response('homepage.html', locals(),
            context_instance=RequestContext(request))

### ### ### ###
import os
from django.conf import settings


def music_library(request):
    caminho = os.path.join(settings.STATIC_ROOT, 'music_list.txt')

    try:
        with open(caminho) as albums:
            lista = albums.read().decode('utf-8', errors='replace')
    except:
        raise Http500

    return render_to_response('music_library.html',
            {'music_list': lista},
            context_instance=RequestContext(request))
### ### ### ###

def seminario_django(request):
    caminho = os.path.join(settings.STATIC_ROOT, 'seminario_django.html')

    try:
        with open(caminho) as arquivo:
            html = arquivo.read()
    except:
        raise Http500

    return HttpResponse(html)
