from django.template import RequestContext, loader
from agenda.models import Contato
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    usuario = request.user
    contato_list = Contato.objects.filter(user=usuario)
    t = loader.get_template('agenda/index.html')
    c = RequestContext(request,
            { 'contato_list': contato_list,
                'usuariosessao': request.user.username})

    return HttpResponse(t.render(c))


@login_required
def detail(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id)
    return render(request, 'agenda/detail.html',
            {'contato': contato})
