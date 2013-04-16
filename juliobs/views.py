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
    mcomp = ("Mat. Comp. - 023582 A", "Politano", "AT9 - 214")
    comp1 = ("Compiladores 1 - 021130 A", "Helena Caseli", "AT9 - 199")
    celet = ("Circuitos Eletrônicos - 024171 A", "Kato", "AT9 - 199")
    l_ele = ("Laboratório de Circuitos Eletrônicos - 024180", "Kato", "DC - 623")
    sd    = ("Sistemas Distribuidos - 025321 B", "Trevelin", "AT7 - 165")
    calc2 = ("Cálculo 2 - 089206 D", "Bruna", "AT9 - 219/213")
    mec    = ("Mecânica Aplicada - 120030 E", "Fernando", "AT5 - 97")

    h = [[nada,  sd,    celet, nada,  comp1],
         [nada,  sd,    celet, nada,  comp1],
         [mcomp, nada,  l_ele, mec,   nada],
         [mcomp, calc2, nada,  calc2, nada],
         [nada,  nada,  nada,  nada,  nada],
         [nada,  nada,  nada,  nada,  nada]]

    return render(request, 'horario.html', {'h': h})
