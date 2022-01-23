#from tkinter import CASCADE
from django.db import models
from datetime import datetime

# Create your models here.

class Servico(models.Model):

    id = models.BigAutoField(db_column='id', primary_key=True, null=False, blank=False,)
    servico = models.CharField(db_column='servico', max_length=100, null=False, blank=False,)
    descricao_servico = models.CharField(db_column='descricao_servico', max_length=512, null=False, blank=False)

    class Meta:
        ordering = ['id']
        db_table = 'servico'

    def __str__(self):
        return self.servico


class Equipe(models.Model):

    id = models.BigAutoField(db_column='id', primary_key=True, null=False, blank=False,)
    nome = models.CharField(db_column='nome', max_length=128, blank=False)
    idade = models.IntegerField(db_column='idade', blank=True, null=True)
    expertise = models.CharField(db_column='expertise', max_length=256, blank=False)
    equipe_servico = models.ForeignKey(Servico, related_name='equipe_servico', on_delete=models.DO_NOTHING)


    class Meta:
        ordering = ['id']
        db_table = 'equipe'

    def __str__(self):
        return self.nome


class Postagem(models.Model):

    id = models.BigAutoField(db_column='id', primary_key = True, null = False, blank=False,)
    data_criacao = models.DateTimeField(db_column='data_criacao', blank=True, null=False, default = datetime.now)
    autor_postagem = models.ForeignKey(Equipe, related_name='autor_postagem', on_delete=models.DO_NOTHING)
    data_postagem = models.DateTimeField(db_column='data_postagem', blank=True, null=True)
    titulo = models.CharField(db_column='titulo', max_length=40, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    tags = models.CharField(db_column='tags', max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id'] 
        db_table = 'postagem'


    def __str__(self):
        return self.titulo




