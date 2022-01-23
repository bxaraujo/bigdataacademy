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



# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def index(request): 
        return HttpResponse("""       
        <h1> Bem-vindo!</h1>
        <h2>Olá, seja bem-vindo a API para gerenciamento do conteúdo do site institucional.</h2>
        <h2>Faça o login em /admin para se autenticar</h2>
        <h3>
            <p>
                <br>Endpoints disponíveis:
                    <br>Painel Administrativo: /admin/</br>
                    Listar todos os serviços: /servicos/
                    <br>Listar apenas um serviço pelo id: /servicos-detalhe/id</br>
                    Listar todos os Integrantes da empresa: /equipe/
                    <br>Listar Integrante específico pelo id: /equipe-detalhe/id</br>
                    Listar todos os Posts: /posts/
                    <br>Listar Post específico: /posts-detalhe/id</br>
            </p>
        </h3>""")

"""
@api_view(['GET', 'POST'])
@swagger_auto_schema(method='POST', request_body = Serializer) """

class ServicoList(generics.ListCreateAPIView):

    """ Este endpoint disponibiliza uma lista dos serviços oferecidos pela Agência Cronos"""

    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ServicoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostagemList(generics.ListCreateAPIView):

    """ Este endpoint disponibiliza uma lista das postagens realizadas pelo autor que faz parte de uma das equipes de serviço"""

    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PostagemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )


class IntegranteEquipeList(generics.ListCreateAPIView):

    """ Este endpoint disponibiliza uma lista de integrantes das equipes de serviço"""
    
    queryset = IntegranteEquipe.objects.all()
    serializer_class = IntegranteEquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )

class IntegranteEquipeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegranteEquipe.objects.all()
    serializer_class = IntegranteEquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly, )
