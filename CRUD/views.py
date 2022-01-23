#from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# rest_framework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import generics

# authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

# Models e Serializers
from .models import Postagem, Servico, IntegranteEquipe
from .serializers import ServicoSerializer, PostagemSerializer, IntegranteEquipeSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def index(request): 
        return HttpResponse("""       
        <h1> Bem-vindo a Cronos API!</h1>
        <h2>Olá, seja bem-vindo a API para gerenciamento do conteúdo do site institucional da Cronos.</h2>
        <h2> Instruções de utilização e Lista de Endpoints disponíveis: <a href="https://github.com/bxaraujo/bigdataacademy#readme"> GitHub - README.md</a> </h2>""")



class ServicoList(generics.ListCreateAPIView):
    """ Este endpoint interage sobre os dos serviços oferecidos pela Agência Cronos"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ServicoDetails(generics.RetrieveUpdateDestroyAPIView):
    """ Este endpoint interage sobre os dos serviços oferecidos pela Agência Cronos"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostagemList(generics.ListCreateAPIView):
    """ Este endpoint interage sobre os Posts escritos pelos integrantes da Agência Cronos"""
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PostagemDetails(generics.RetrieveUpdateDestroyAPIView):
    """ Este endpoint interage sobre os Posts escritos pelos integrantes da Agência Cronos"""
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class IntegranteEquipeList(generics.ListCreateAPIView):
    """ Este endpoint interage sobre os Integrantes das Equipes da Agência Cronos"""
    queryset = IntegranteEquipe.objects.all()
    serializer_class = IntegranteEquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )

class IntegranteEquipeDetails(generics.RetrieveUpdateDestroyAPIView):
    """ Este endpoint interage sobre os Integrantes das Equipes da Agência Cronos"""
    queryset = IntegranteEquipe.objects.all()
    serializer_class = IntegranteEquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )
