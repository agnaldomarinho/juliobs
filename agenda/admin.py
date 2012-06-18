from agenda.models import Contato
from django.contrib import admin


class ContatoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacoes pessoais', {'fields':['nome', 'endereco', 'sexo']}),
        ('Informacoes de contato', {'fields':['email', 'tel', 'url']}),
        ('Usuario ao qual o contato esta associado', {'fields':['user']}),
    ]

    list_display = ('nome', 'email', 'user')
    list_filter = ['user']
    search_fields = ['nome']

admin.site.register(Contato, ContatoAdmin)
