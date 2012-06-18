from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
    GENEROS_DISP = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    user = models.ForeignKey(User)
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    tel = models.IntegerField('Numero de telefone')
    url = models.URLField('Website', blank=True)
    sexo = models.CharField(max_length=1, choices=GENEROS_DISP)

    def __unicode__(self):
        return self.nome
