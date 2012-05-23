from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView

from torrents.views import torrents
from projetos.views import projetos, programas
from ira.views import ira

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^blog/(?P<post>.*)$',
        RedirectView.as_view(url='http://blog.juliobs.com/%(post)s', permanent=True)),

    (r'^$', homepage),
    (r'^torrents/$', torrents),
    (r'^projetos/$', projetos),
    (r'^projetos/(.*)$', programas),
    (r'^ira/$', ira),

  # Robots & Humans
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),
    (r'^humans.txt$', TemplateView.as_view(template_name='humans.txt')),
    (r'^erro_500$', TemplateView.as_view(template_name='500.html')),
    (r'^erro_404$', TemplateView.as_view(template_name='404.html')),
)
