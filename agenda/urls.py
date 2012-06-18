from django.conf.urls import patterns, include, url

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index'),
    url(r'^(?P<contato_id>\d+)/$', 'detail'),
)
