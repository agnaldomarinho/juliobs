#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Wed, 14 Dec 2011 19:32:33 -0200

"""
PyGrad
Baixa o histórico disponível no ProgradWeb e realiza o cálculo do IRA
automaticamente.

Opcionalmente, gera um arquivo CSV que pode ser editado e usado como input de
outro programa. Útil para prever o IRA quando as notas ainda não foram
digitadas.

Com algumas versões do SSL o link HTTPS não funciona bem, basta descomentar
o que usa http e comentar o que usa https.
"""
__author__ = "Julio Batista Silva"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.1"

import sys
import argparse
import getpass
import re
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from math import ceil
import csv


def main(ra, senha, arquivos):

    if not ra:
        ra = raw_input("Digite seu RA: ")

    if not senha:
        senha = getpass.getpass("Senha: ")

    br = Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.addheaders = [('User-agent',
        'Mozilla/5.0 (X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1')]

    #link = 'https://progradweb.ufscar.br/progradweb/servlet/Superior'
    link = 'http://progradweb.ufscar.br:8080/progradweb/servlet/Superior'
    br.open(link)
    br.select_form(name="fSuperior")
    br.form["Usuario"] = ra
    br.form["sess"] = senha
    br.submit()

    br.select_form(name="fPrincipal")
    resp = br.submit()
    #Corrige nested FORMs
    soup = BeautifulSoup(resp.get_data())
    resp.set_data(soup.prettify())
    br.set_response(resp)

    br.select_form(name="fHistorico")
    pagina = br.submit()

    data = pagina.get_data()

    # Possui mais de 1 enfase?
    if data.find("Clique em uma das &ecirc;nfases abaixo para ver o") != -1:
        links = list(br.links(url_regex=re.compile(r"^javascript:submita")))

        print 'Enfases:'
        for index, link in enumerate(links, start=1):
            print '({}) - {}'.format(index, link.text)

        n = int(raw_input("Digite o numero da enfase: "))

        pattern = re.compile(r'''
        javascript:submita\(\'
        (\d*)\',%20\'
        (\d*)\',%20\'
        (\d)
        ''', re.VERBOSE)

        enfase, ano, semestre = pattern.search(links[n - 1].url).groups()

        br.back()
        br.select_form(name="fHistorico")

        br.form.new_control('text', 'RA', {'value': ra})
        br.form.new_control('text', 'Enfase', {'value': enfase})
        br.form.new_control('text', 'AnoIni', {'value': ano})
        br.form.new_control('text', 'SemIni', {'value': semestre})
        br.form.new_control('text', 'Tipo', {'value': '1'})
        br.form.new_control('text', 'MaisEnfase', {'value': 'S'})
        br.form.new_control('text', 'Modo', {'value': '2'})
        br.form.new_control('text', 'CodigoCurso', {'value': ''})
        br.form.new_control('text', 'Certificado', {'value': '0'})
        br.form.new_control('text', 'Consulta', {'value': '0'})
        br.form.new_control('text', 'sC', {'value': '51'})
        br.form.fixup()
        pagina = br.submit()

    html = BeautifulSoup(pagina.get_data())
    linhas = html.findAll('tr')

    creditos_aprovados = 0
    creditos_solicitados = 0
    creditos_desistentes = 0
    creditos_trancados = 0
    creditos_reprovados = 0
    nota_ponderada = 0

    if arquivos:
        materias = []

    for lin in linhas:
        if len(lin) == 21:
            materia = lin.findAll('td')

            nome = materia[2].text.encode('utf-8')
            nota = materia[3].text
            if nota == '&nbsp;':
                nota = 0
            nota = float(nota)

            resultado = materia[5].text
            creditos = int(materia[6].text)

            if arquivos:
                materia = {'nome': nome,
                        'nota': nota,
                        'resultado': resultado,
                        'creditos': creditos}
                materias.append(materia)

            if resultado == 'Aprovado':
                creditos_aprovados += creditos
            elif resultado == 'Cancelado':
                creditos_solicitados -= creditos
                creditos_trancados += creditos
            elif (resultado == 'Reprovado nota' or
                    resultado == 'Reprovado nota/freq.' or
                    resultado == 'Pendente'):
                creditos_reprovados += creditos
            elif resultado == 'Desistente':
                creditos_desistentes += creditos
            elif resultado == 'Afastado':
                creditos -= creditos

            creditos_solicitados += creditos
            nota_ponderada += creditos * nota

    # Realiza o cálculo
    ira = ((nota_ponderada / creditos_solicitados) *
            (2 - 2 * (creditos_desistentes / creditos_solicitados) -
                creditos_trancados / creditos_solicitados)) * 1000
    ira = int(ceil(ira))

    print "Seu ira é {}.".format(ira)

    if arquivos:
        keys = ['nome', 'nota', 'resultado', 'creditos']
        for arquivo in arquivos:
            out = csv.DictWriter(arquivo, keys)
            out.writer.writerow(keys)
            out.writerows(materias)
        
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Calcula seu IRA automaticamente.',
            epilog='''Este programa solicita sua senha, pois ele acessa o site
            do ProGrad Web, baixa seu histórico e realiza os cálculos.''')
    parser.add_argument('-ra', '--ra', type=str, help='Número do RA')
    parser.add_argument('-pass', '--senha', type=str, help='Senha do ProGrad')
    parser.add_argument('-v', '--verbose', dest='arquivos',
            action='append_const', const=sys.stdout,
            help='Imprime histórico na tela')
    parser.add_argument('-f', '--file', dest='arquivos', action='append',
            type=argparse.FileType('wb'),
            help='Nome do arquivo csv onde o histórico será salvo')

    args = parser.parse_args()

    main(args.ra, args.senha, args.arquivos)
