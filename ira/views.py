# -*-*- encoding: utf-8 -*-*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from BeautifulSoup import BeautifulSoup
import re
import mechanize

c_inscritos = 0
c_desist = 0
c_cancel = 0
nota_ponderada = 0
result_opts = ["Afastado", "Aprovado", "Reprovado", "Cancelado", "Desistente", "Pendente"]


### Faz login. Retorna a página principal
def login_prograd(ra, senha):
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/19.0 Firefox/19.0')]

    link = 'https://progradweb.ufscar.br/progradweb/servlet/Superior'

    try:
        br.open(link)
        br.select_form(name="fSuperior")
        br.form["Usuario"] = ra
        br.form["sess"] = senha
        br.submit()

        br.select_form(name="fPrincipal")
        resp = br.submit()
    except mechanize._mechanize.FormNotFoundError:
        return False
    except:
        return False
    else:
        #Corrige nested FORMs
        soup = BeautifulSoup(resp.get_data())
        resp.set_data(soup.prettify())
        br.set_response(resp)

        return br


def abre_historico(br, ra, enfase='0', ano='0', semestre='1'):
    br.select_form(name="fHistorico")
    #Recria form. A página continua quebrada mesmo com BeautifulSoup
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
    br.submit()

    return br


## Retorna lista vazia se tiver apenas uma ênfase
def multiplas_enfases(br):
    enfases = []
    data = br.response().read()
    if data.find("Clique em uma das &ecirc;nfases abaixo para ver") != -1:
        links = list(br.links(url_regex=re.compile(r"^javascript:submita")))
        for link in links:
            nome = link.text.decode('ISO-8859-1')
            enfase = {'nome': nome, 'url': link.url}
            enfases.append(enfase)
    return enfases


# Cria lista de matérias a partir de um html (BeautifulSoup)
def parse_html(html):
    linhas = html.findAll('tr')
    materias = []
    for lin in linhas:
        if len(lin) == 21:
            materia = lin.findAll('td')
            nome = materia[1].text + " - " + materia[2].text
            nota = materia[3].text
            resultado = materia[5].text
            creditos = int(materia[6].text)
            materia = processa_materia(nome, nota, resultado, creditos)
            materias.append(materia)

    # Cria matéria vazia para evitar problemas com script de linhas (bixos)
    materia_vazia = {'nome': '', 'nota': '', 'resultado': '', 'creditos': ''}
    materias.append(materia_vazia)

    return materias


# Cria um dicionário com as informações de uma matéria
def processa_materia(nome, nota, resultado, creditos):
    global c_inscritos
    global c_desist
    global c_cancel
    global nota_ponderada

    if nota == '&nbsp;' or nota == '':
        nota = '0.0'
    nota = float(nota.replace(',', '.'))  # corrige locale
    creditos = int(creditos)

    if resultado != 'Afastado':
        c_inscritos += creditos

        if resultado == 'Aprovado':
            nota_ponderada += creditos * nota
        elif (resultado == 'Reprovado nota' or
                resultado == 'Reprovado nota/freq.' or
                resultado == 'Reprovado'):
            resultado = 'Reprovado'
            nota_ponderada += creditos * nota
        elif resultado == 'Pendente':
            nota_ponderada += creditos * nota
        elif resultado == 'Cancelado':
            c_cancel += creditos
            c_inscritos -= creditos / 2  # chutometro
        elif resultado == 'Desistente':
            c_desist += creditos
        elif resultado == 'Reconhecido':
            nota = 6.0
            nota_ponderada += creditos * nota

    materia = {'nome': nome, 'nota': nota, 'resultado': resultado,
               'creditos': creditos}

    return materia


def calcula_ira(nota_pond, inscr, cancel, desist):
    if inscr <= 0:
        return 0

    try:
        ira = 1000 * (nota_pond / inscr) * (2 - (cancel + 2 * desist) / inscr)
        ira = int(round(ira))
    except:
        ira = 0

    return ira


# Aluno escolheu uma ênfase. Faz login novamente e acessa o histórico.
# TODO: achar um jeito de não precisar novo login
def enfase(request):
    ra = request.session['ra']
    senha = request.session['senha']

    br = login_prograd(ra, senha)

    enfases_link = request.POST['enfase_opt']
    pattern = re.compile(r'''
    javascript:submita\(\'
    (\d*)\',%20\'
    (\d*)\',%20\'
    (\d)
    ''', re.VERBOSE)

    enfase, ano, semestre = pattern.search(enfases_link).groups()
    br = abre_historico(br, ra, enfase, ano, semestre)
    html = BeautifulSoup(br.response().read())
    materias = parse_html(html)

    ira = calcula_ira(nota_ponderada, c_inscritos, c_cancel, c_desist)

    return render(request, 'ira/historico.html',
                  {'ira': ira, 'materias': materias,
                      'resultados_possiveis': result_opts})


# Faz login, verifica multiplas ênfases e mostra histórico
def login(request):
    if request.method == 'GET':
        return HttpResponseRedirect("/ira/")

    if request.method == 'POST':
        ra = request.POST['ra']
        senha = request.POST['senha']

        try:
            br = login_prograd(ra, senha)
            br = abre_historico(br, ra)
            enfases = multiplas_enfases(br)
        except:
            return HttpResponseRedirect("/ira/")

        if enfases:
            request.session['ra'] = ra
            request.session['senha'] = senha
            return render(request, 'ira/enfase.html', {'enfases': enfases})

        html = BeautifulSoup(br.response().read())
        materias = parse_html(html)

        ira = calcula_ira(nota_ponderada, c_inscritos, c_cancel, c_desist)

        return render(request, 'ira/historico.html',
                      {'ira': ira, 'materias': materias,
                          'resultados_possiveis': result_opts})


# Retorna matérias submetidas pelo form de prever IRA
def previsao(nomes, notas, resultados, cred):
    from itertools import izip
    materias = []
    for nome, nota, resultado, creditos in (izip(nomes, notas, resultados, cred)):
        if nome == '':
            nome = 'Digite um nome!'
        if creditos == '':
            creditos = 0
        materia = processa_materia(nome, nota, resultado, creditos)
        materias.append(materia)
    return materias


# Mostra tabela com o histórico alterado
def prever(request):
    if request.method == 'GET':
        return HttpResponseRedirect("/ira/")

    if request.method == 'POST':
        nomes = request.POST.getlist('nome')
        notas = request.POST.getlist('nota')
        resultados = request.POST.getlist('resultado')
        creditos = request.POST.getlist('creditos')

        materias = previsao(nomes, notas, resultados, creditos)

        ira = calcula_ira(nota_ponderada, c_inscritos, c_cancel, c_desist)

        return render(request, 'ira/historico.html',
                      {'ira': ira, 'materias': materias,
                       'resultados_possiveis': result_opts})


# Mostra tabela com o histórico upado
def html_upload(request):
    html = BeautifulSoup(request.POST['hist_html'])
    materias = parse_html(html)

    ira = calcula_ira(nota_ponderada, c_inscritos, c_cancel, c_desist)

    return render(request, 'ira/historico.html',
                  {'ira': ira, 'materias': materias,
                   'resultados_possiveis': result_opts})
