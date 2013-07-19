#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-

"""
Meus views
"""
__author__ = "Julio Batista Silva"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"

from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage.html', {})


def seminario_django(request):
    caminho = os.path.join(settings.STATIC_ROOT, 'seminario_django.html')

    try:
        with open(caminho) as arquivo:
            html = arquivo.read()
    except:
        raise Http500

    return HttpResponse(html)
### ### ### ###


def horario(request):
    ## Se alguma matéria tiver duas salas diferentes crie duas variáveis
    nada  = ("-", "-", "-")

    h = [[nada, nada, nada, nada, nada],
         [nada, nada, nada, nada, nada],
         [nada, nada, nada, nada, nada],
         [nada, nada, nada, nada, nada],
         [nada, nada, nada, nada, nada],
         [nada, nada, nada, nada, nada]]

    return render(request, 'horario.html', {'h': h})
