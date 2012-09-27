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

    return render(request, 'music_library.html', {'music_list': lista})
### ### ### ###


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
    bd    = ("Banco de Dados - 025216 A", "Renato Bueno", "AT9 - 217")
    mic   = ("Microcontroladores - 27278 A", "Paulo Politano", "AT9 - 199")
    so2   = ("SO2 - 021288 A", "Helio Guardia", "DC - Lab. 4")
    lfa   = ("LFA - 020265 A", "Hermes Senger", "AT5 - 114")
    ia    = ("Inteligência Artificial - 022705 A", "Lúcia Rino", "AT9 - 212")
    a_inv = ("Análise de Investimentos - 110159 A", "Andrei Albuquerque", "AT7 - 162")
    cg    = ("Computação Gráfica - 025526 B", "Mário Lizier", "AT9 - 212")
    l_mic = ("Lab Microcontroladores - 027286 B", "Edilson Kato", "DC - 622")
    projm = ("Proj. e Manufatura Assist. por Comp. - 027260 A", "Paulo Politano", "DC - LP01 - SAP")

    h = [[nada,  bd,    mic,   so2,   lfa],
         [nada,  bd,    mic,   so2,   lfa],
         [ia,    nada,  a_inv,  projm, cg],
         [ia,    nada,  l_mic, projm, cg],
         [nada,  nada,  nada,  nada,  nada],
         [nada,  nada,  nada,  nada,  nada]]

    return render(request, 'horario.html', {'h': h})
