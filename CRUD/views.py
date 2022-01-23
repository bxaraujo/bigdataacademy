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
from .models import Postagem, Servico, Equipe
from .serializers import ServicoSerializer, PostagemSerializer, EquipeSerializer



# Create your views here.
""" 
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
 """
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
    permission_classes = (IsAuthenticated, )


class PostagemList(generics.ListCreateAPIView):

    """ Este endpoint disponibiliza uma lista das postagens realizadas pelo autor que faz parte de uma das equipes de serviço"""

    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class PostagemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class EquipeList(generics.ListCreateAPIView):

    """ Este endpoint disponibiliza uma lista de integrantes das equipes de serviço"""
    
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class EquipeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
