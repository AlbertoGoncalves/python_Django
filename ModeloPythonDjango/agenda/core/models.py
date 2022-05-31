from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    # max_length=100 tamanho de no maixo 100 Caracteres
    descricao = models.TextField(blank=True,null=True)
    # TextField() tamanho indeterminado
    #blank=True pode ser em branco ,null=True pode ser nulo
    dataEvento = models.DateTimeField(verbose_name='Data do evento')
    # verbose_name para definir no do campo visual
    dataCriacao = models.DateTimeField(auto_now=True,verbose_name='Data de criação')
    # auto_now=True usado para ja informar data hora atual
    # para transformar essa class em tabela necessario executar comando migrate
    # comando: python manage.py makemigrations core
    # cria um arquivo de migração dentro da pasta migrations
    # para criar de fato no banco rodar python manage.py migrate core 0001

    #como add uma dependencia com outra tabela
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    #on_delete=models.CASCADE se o usuario for excluido exclui tudo dele
    #necessario importar models do django
    #from django.contrib.auth.models import User

    #para verificar se houve alteracoes na tabela para migrar
    #Comando: python manage.py makemigrations core
    #sera gerado novo arquivo em migrations


    #definindo nome da tabela
    class Meta:
        db_table = 'evento'

    #Comando para na listagem trazer o titulo
    def __str__(self):
        return self.titulo

