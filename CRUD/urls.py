#from django.conf.urls import patterns, url
from django.urls import path
from .views import *

#app_name = 'cronos'
urlpatterns = [
    #path('', url(r'^$', views.index, name='index')), 
    path('', index, name='index'), 
    path(r'servicos/', ServicoList.as_view(), name='Lista de Serviços'),
    path(r'servicos/<int:pk>', ServicoDetails.as_view(), name='Seleção do Serviço pelo id'),

    path(r'posts/', PostagemList.as_view(), name='Lista de Posts'),
    path(r'posts/<int:pk>', PostagemDetails.as_view(), name='Seleção do Post pelo id'),

    path(r'integranteequipe/', IntegranteEquipeList.as_view(), name='Lista de Integrantes da Equipe'),
    path(r'integranteequipe/<int:pk>', IntegranteEquipeDetails.as_view(), name='Seleção do Integrante da Equipe por id'),
    
]
