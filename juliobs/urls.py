# -*-*- encoding: utf-8 -*-*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import *
from django.views.generic.base import TemplateView, RedirectView
from django.http import HttpResponse

from views import *
from torrents.views import torrents
from projetos.views import projetos, programas
from contato.views import contact


class PlainTextView(TemplateView):
    """A plain text generic template view."""
    def render_to_response(self, context, **kwargs):
        return super(PlainTextView, self).render_to_response(
                                context, content_type='text/plain', **kwargs)

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^i18n/', include('django.conf.urls.i18n')),
        (r'^blog/(?P<post>.*)$',
            RedirectView.as_view(url='http://blog.juliobs.com/%(post)s', permanent=True)),
        url(r'^$', homepage, name="jbs-home"),
        url(r'^music_library/$', music_library, name="jbs-music_lib"),
        url(r'^horario/$', horario, name="jbs-horario"),
        url(r'^licenca/$', TemplateView.as_view(template_name='licenca.html'),
            name="jbs-licenca"),
        url(r'^pgp/$', TemplateView.as_view(template_name='public_key.html'),
            name="jbs-pgp"),
        url(r'^qrcode/$', TemplateView.as_view(template_name='qrcode.html'),
            name="jbs-qrcode"),
        url(r'^projetos/$', projetos, name="jbs-projetos"),
        (r'^projetos/(.*)$', programas),
        (r'^cv/$', TemplateView.as_view(template_name='curriculum.html')),
        (r'^stuff-i-use/$', TemplateView.as_view(template_name='stuff_i_use.html')),
        (r'^torrents/$', torrents),
        (r'^ira/', include('ira.urls', namespace='ira')),
        url(r'^contato/$', contact, name="jbs-contato"),
        (r'^contato/ok/$', TemplateView.as_view(template_name='contato_ok.html')),
        (r'^gallery/', include('imagestore.urls', namespace='imagestore')),
        url(r'^agenda/', include('agenda.urls')),

        url(r'^accounts/login/$',  login),
        url(r'^accounts/logout/$', logout),
        url(r'^accounts/password_change/$', password_change),
        url(r'^accounts/password_change_done/$', password_change_done),
        (r'^accounts/password_reset/$', 'password_reset'),

        (r'^seminario/$', seminario_django),
        (r'^cg_t4/', include('cg_t4.urls', namespace='cg_t4')),
)

urlpatterns += patterns('',
        # Robots & Humans
        (r'^humans.txt$', PlainTextView.as_view(template_name='humans.txt')),
        url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *",
        mimetype="text/plain")),
        url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
        
        # Para testar páginas de erro
        (r'^erro_500$', TemplateView.as_view(template_name='500.html')),
        (r'^erro_404$', TemplateView.as_view(template_name='404.html')),
)

# Não manda email sobre erros 404 que seguem alguns padrões
import re
IGNORABLE_404_URLS = (re.compile(r'^/apple-touch-icon.*\.png$'),)
