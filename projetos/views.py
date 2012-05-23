# -*-*- encoding: utf-8 -*-*-
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from pygments import highlight
from pygments.lexers import guess_lexer, guess_lexer_for_filename, TextLexer
from pygments.formatters import HtmlFormatter

programas_dir = os.path.join(settings.STATIC_ROOT, 'Programas')


def projetos(request):
    sites = [{'nome':'Sugere Discos', 'link':'/sugere_discos'},
            {'nome':'Traduzator (Babylon)', 'link':'/traduzator'},
            {'nome':'Calculador de IRA', 'link':'/ira'},
            {'nome':'Gerador de Currículo', 'link':'/gera_curriculo'}]

    programas = []
    for root, dirnames, filenames in os.walk(programas_dir):
        for filename in filenames:
            (nome, ext) = os.path.splitext(filename)
            caminho = os.path.relpath(root, programas_dir)
            link = os.path.join(caminho, filename)
            programas.append({'nome': nome, 'linguagem': ext, 'link': link})

    return render_to_response('projetos.html',
            {'sites': sites, 'programas': programas},
            context_instance=RequestContext(request))


def programas(request, arquivo):
    erros = False
    codigo = ''
    nome = 'Erro!'

    caminho = os.path.join(programas_dir, arquivo)

    if os.path.isfile(caminho):
        try:
            with open(caminho) as programa:
                texto = programa.read().decode('utf-8')
        except IOError:
            erros = True
        else:
            nome = os.path.basename(arquivo)

            #Se não conseguir adivinhar a linguagem do programa exibe texto
            try:
                lexer = guess_lexer_for_filename(arquivo, texto)
            except ValueError:
                try:
                    lexer = guess_lexer(texto)
                except ValueError:
                    lexer = TextLexer

            # linenos pode ser inline, table, True ou ''
            codigo = highlight(texto, lexer, HtmlFormatter(linenos='inline'))
    else:
        erros = True

    return render_to_response('programas.html',
            {'erros': erros, 'nome': nome, 'codigo': codigo},
            context_instance=RequestContext(request))
