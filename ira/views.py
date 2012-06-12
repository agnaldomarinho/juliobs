# -*-*- encoding: utf-8 -*-*-
from django.shortcuts import render_to_response
from django.template import RequestContext
import re
import mechanize
from BeautifulSoup import BeautifulSoup
import socket
import sys


def ira(request):
    #Se acabou de entrar no site
    if request.method == 'GET':
        return render_to_response('ira.html',
                {'etapa': 'login'},
                context_instance=RequestContext(request))
    #Se já digitou RA e Senha
    elif request.method == 'POST':
        if 'login' in request.POST:
            errors = []
            if not request.POST.get('ra', ''):
                errors.append('Digite um RA valido.')
            if not request.POST.get('senha', ''):
                errors.append('Digite uma senha valida.')

            #RA ou senha em branco
            if errors:
                return render_to_response('ira.html',
                        {'etapa': 'login',
                            'errors': errors},
                        context_instance=RequestContext(request))
            else:
                ra = request.POST['ra']
                senha = request.POST['senha']

                br = mechanize.Browser()
                br.set_handle_equiv(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)

                br.addheaders = [('User-agent',
                    'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0')]

                link = 'https://progradweb.ufscar.br/progradweb/servlet/Superior'

                try:
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
                    #Recria form. A página continua quebrada mesmo com BeautifulSoup
                    br.form.new_control('text', 'RA', {'value': ra})
                    br.form.new_control('text', 'Enfase', {'value': '0'})
                    br.form.new_control('text', 'AnoIni', {'value': '2009'})
                    br.form.new_control('text', 'SemIni', {'value': '1'})
                    br.form.new_control('text', 'Tipo', {'value': '1'})
                    br.form.new_control('text', 'MaisEnfase', {'value': 'S'})
                    br.form.new_control('text', 'Modo', {'value': '2'})
                    br.form.new_control('text', 'CodigoCurso', {'value': ''})
                    br.form.new_control('text', 'Certificado', {'value': '0'})
                    br.form.new_control('text', 'Consulta', {'value': '0'})
                    br.form.new_control('text', 'sC', {'value': '51'})
                    br.form.fixup()
                    pagina = br.submit()
                    data = pagina.get_data()
                except mechanize._mechanize.FormNotFoundError:
                    errors.append('Verifique sua senha.')
                    return render_to_response('ira.html',
                            {'etapa': 'login',
                                'errors': errors},
                            context_instance=RequestContext(request))
                except:
                    errors.append(sys.exc_info())
                    return render_to_response('ira.html',
                            {'etapa': 'login',
                                'errors': errors},
                            context_instance=RequestContext(request))
                else:
                    #Possui mais de 1 enfase?
                    if data.find("Clique em uma das &ecirc;nfases abaixo para ver o") != -1:
                        #Se não escolheu a enfase na etapa anterior
                        if not request.POST.get('enfase_opt', ''):
                            links = list(br.links(
                                url_regex=re.compile(r"^javascript:submita")))

                            enfases = []
                            for link in links:
                                nome = link.text.decode('ISO-8859-1')
                                enfase = {'nome': nome,
                                        'url': link.url}
                                enfases.append(enfase)

                            return render_to_response('ira.html',
                                    {'enfases': enfases,
                                        'ra': ra,
                                        'senha': senha,
                                        'etapa': 'selecionar_enfase'},
                                    context_instance=RequestContext(request))
                        #Já escolheu uma ênfase
                        else:
                            enfases_link = request.POST['enfase_opt']
                            pattern = re.compile(r'''
                            javascript:submita\(\'
                            (\d*)\',%20\'
                            (\d*)\',%20\'
                            (\d)
                            ''', re.VERBOSE)

                            enfase, ano, semestre = pattern.search(enfases_link).groups()

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

                    #Filtra página do histórico escolar
                    html = BeautifulSoup(pagina.get_data())
                    linhas = html.findAll('tr')

                    creditos_inscritos = 0
                    creditos_desistentes = 0
                    creditos_cancelados = 0
                    nota_ponderada = 0

                    materias = []
                    for lin in linhas:
                        if len(lin) == 21:
                            materia = lin.findAll('td')

                            nome = materia[1].text + " - " + materia[2].text
                            nota = materia[3].text
                            resultado = materia[5].text
                            creditos = int(materia[6].text)

                            if nota == '&nbsp;':
                                nota = 0
                            nota = float(nota)

                            if resultado != 'Afastado':
                                creditos_inscritos += creditos

                                if resultado == 'Aprovado':
                                    nota_ponderada += creditos * nota
                                elif (resultado == 'Reprovado nota' or
                                        resultado == 'Reprovado nota/freq.' or
                                        resultado == 'Pendente'):
                                    nota_ponderada += creditos * nota
                                elif resultado == 'Cancelado':
                                    creditos_cancelados += creditos
                                    creditos_inscritos -= creditos / 2  # chutometro
                                elif resultado == 'Desistente':
                                    creditos_desistentes += creditos
                                elif resultado == 'Reconhecido':
                                    nota = 6.0
                                    nota_ponderada += creditos * nota

                            # Guarda lista para depois
                            materia = {'nome': nome,
                                    'nota': nota,
                                    'resultado': resultado,
                                    'creditos': creditos}
                            materias.append(materia)

                    # Se ainda não fez nenhuma disciplina (bixo) faz ira = 0 e
                    # preenche tabela com uma linha para não dar problema com o
                    # script de adicionar e deletar linhas
                    if (creditos_inscritos <= 0):
                        ira = 0
                        materia = {'nome': '',
                                'nota': '',
                                'resultado': '',
                                'creditos': ''}
                        materias.append(materia)
                    else:
                        try:
                            ira = 1000 * (nota_ponderada / creditos_inscritos) * (2 -
                                    (creditos_cancelados + 2 * creditos_desistentes) / creditos_inscritos)
                            ira = int(round(ira))
                        except:
                            errors.append(sys.exc_info())
                            return render_to_response('ira.html',
                                    {'etapa': 'login',
                                        'errors': errors},
                                    context_instance=RequestContext(request))

                    return render_to_response('ira.html',
                            {'etapa': 'mostrar_ira',
                                'ira': ira,
                                'materias': materias},
                            context_instance=RequestContext(request))

        elif 'previsao' in request.POST:
            from itertools import izip

            nomes = request.POST.getlist('nome')
            notas = request.POST.getlist('nota')
            resultados = request.POST.getlist('resultado')
            cred = request.POST.getlist('creditos')

            creditos_inscritos = 0
            creditos_desistentes = 0
            creditos_cancelados = 0
            nota_ponderada = 0

            materias = []
            for nome, nota, resultado, creditos in (izip(nomes, notas, resultados, cred)):
                if nome == '':
                    nome = 'Digite um nome!'

                if resultado != 'Afastado':
                    try:
                        creditos = int(creditos)
                    except:
                        creditos = 0
                    try:
                        nota = float(nota.replace(',', '.'))  # corrige locale
                    except:
                        nota = 0

                    creditos_inscritos += creditos

                    if resultado == 'Aprovado':
                        nota_ponderada += creditos * nota
                    elif (resultado == 'Reprovado nota' or
                            resultado == 'Reprovado nota/freq.' or
                            resultado == 'Pendente'):
                        nota_ponderada += creditos * nota
                    elif resultado == 'Cancelado':
                        creditos_cancelados += creditos
                        creditos_inscritos -= creditos / 2  # chutometro
                    elif resultado == 'Desistente':
                        creditos_desistentes += creditos
                        creditos_inscritos += creditos  # chutometro
                    elif resultado == 'Reconhecido':
                        nota = 6.0
                        nota_ponderada += creditos * nota

                # Guarda lista para depois
                materia = {'nome': nome,
                        'nota': nota,
                        'resultado': resultado,
                        'creditos': creditos}
                materias.append(materia)

            # Se ainda não fez nenhuma disciplina (bixo) faz ira = 0 e
            # preenche tabela com uma linha para não dar problema com o
            # script de adicionar e deletar linhas
            if (creditos_inscritos <= 0):
                ira = 0
                materia = {'nome': '',
                        'nota': '',
                        'resultado': '',
                        'creditos': ''}
                materias.append(materia)
            else:
                try:
                    ira = 1000 * (nota_ponderada / creditos_inscritos) * (2 -
                            (creditos_cancelados + 2 * creditos_desistentes) / creditos_inscritos)
                    ira = int(round(ira))
                except:
                    errors.append(sys.exc_info())
                    return render_to_response('ira.html',
                            {'etapa': 'login',
                                'errors': errors},
                            context_instance=RequestContext(request))

            return render_to_response('ira.html',
                    {'etapa': 'mostrar_ira',
                        'ira': ira,
                        'materias': materias},
                    context_instance=RequestContext(request))
