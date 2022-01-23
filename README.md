# Desafio Deloitte + Gama Academy 
## BIG DATA ACADEMY - CASE TÉCNICO
![alt text](https://github.com/bxaraujo/bigdataacademy/blob/e80064f9bd924f7040131d796f839fb8c04bd02b/miscellaneous/logo-gama.svg "Gama Academy 1")

Desafio técnico proposto pela Gama Academy em parceria om a deloitte. 
Para realizar este case técnico, optei por seguir o desafio do BACKEND, visto que tenho mais conhecimento e prática nesta área.
A proposta foi construir uma API REST para gerenciamento do conteúdo do site institucional de um cliente fictício chamado Cronos.


## Tecnologias utilizadas

* Python
* Django + Django Rest Framework
* SQLite
* PostgreSQL
* Heroku
* drf_yasg

### Python
Optei por utilizar o python para realizar o desafio por ter mais experiência com esta linguagem

### Django + Django Rest Framework
A utilização do Django como framework para desenvolvimento da aplicação WEB e Django Rest Framework devido as particularidades do desafio em solicitar uma API Rest.
O Django com o django rest framework nos trás uma grande quantidade de ferramentas que facilitam o desenvolvimento de REST APIs como serializadores, modelos e views, assim como banco de dado e servidor integrado para ambiente de desenvolvimento. 
Além disso também possui facilidades para autenticação e permissões, assim como painel administrativo de setup facilitado.

### SQLite
Banco de dados relacional utilizado para ambiente de desenvolvimento e também para o commit no GitHub, visto que sua estrutura simples em formato de arquivo é de fácil utilização e possível de rodar localmente.

### Heroku
Decidi utilizar o heroku como ferramenta e PaaS para deploy da API em produção.

### PostgreSQL
Banco de dados relacional, bastante robusto e confiável, utilizado para o ambiente de produção.

### drf_yasg
Para documentar a API escolhi utilizar o drf_yasg, pacote muito útil que documenta a REST API desenvolvida com o django rest framework nos formatos mais utilizados no mercado como OPENAPI e REDOC.


## Baixar o código-fonte do projeto
```
git clone https://github.com/bxaraujo/bigdataacademy.git
```
>Rodar o projeto localmente é impossível uma vez que se observa a inexistência de variáveis de ambiente que contêm informações sigilosas tais como as URI's de conexão com o Banco de Dados. Alternativas para testar a aplicação são descritas logo abaixo.


## Utilização da solução

O servidor Back-End está hospedado na Heroku, logo todas as suas rotas podem ser acessadas partindo do link:
```
**https://cronos-rest-api.herokuapp.com/**
```
### Login e autenticação simples

Acessar a rota:
```
/admin/
```
Para administrar o conteúdo via painel de gerenciamento, utilizar o usuário **admin** e a senha **Cronosadmin**.

## Rotas para Documentação OPENAPI, REDOC e SWAGGER
```
/swagger.json
/swagger.yaml
/swagger/
/redoc/
```
## Rotas

O servidor Back-End está hospedado na Heroku, logo todas as suas rotas podem ser acessadas partindo do link:
https://employees-server.herokuapp.com/


### Rotas do CRUD de Serviços
#### Rotas GET
##### Obter lista de Serviços:
```
/servicos/
```
##### Obter lista de Integrantes da Equipe:
```
/integranteequipe/
```
##### Obter lista de Posts:
```
/posts/
```

#### Rotas POST
##### Criar novo Serviço:
```
/servicos/
```
Cria um novo serviço no banco de dados que poderá ser utilizado para atrelar novos integrantes de equipe a este.

O corpo da requisição deve conter o campo **servico** e **descricao_servico** como mostra o JSON abaixo:
```
{
  "servico": "string",
  "descricao_servico": "string"
}
```
##### Criar novo Integrante da Equipe:
```
/integranteequipe/
```

Cria um novo integrante no banco de dados que poderá ser utilizado para atrelar posts a este.

O corpo da requisição deve conter o campo **nome**, **idade**, **expertise** e a **equipe_servico** (id proveniente dos serviços ofertados) como mostra o JSON abaixo:
```
{
  "nome": "string",
  "idade": 0,
  "expertise": "string",
  "equipe_servico": 0
}
```
##### Criar novo Post:
```
/posts/
```
Cria um novo post no banco de dados.

O corpo da requisição deve conter o campo **data_criacao**, **data_postagem**, **titulo**, **texto**, **tags** e **autor_postagem**  (que é o id proveniente dos Integrantes da Equipe) como mostra o JSON abaixo:
```
{
  "data_criacao": "2022-01-23T22:14:11.270Z",
  "data_postagem": "2022-01-23T22:14:11.270Z",
  "titulo": "string",
  "texto": "string",
  "tags": "string",
  "autor_postagem": 0
}
```

#### Rotas PUT
Para executar o método PUT é necessário utilizar o envio do corpo igual aos modelos utilizados no método POST.

##### Atualizar serviço específico:
```
/servicos/:servicoId
```
Substitua :servicoId pelo Id do serviço que deseja atualizar e voilà!

##### Obter lista de Integrantes da Equipe:
```
/integranteequipe/:integranteId
```
Substitua :integranteId pelo Id do integrante da equipe que deseja atualizar e voilà!

##### Obter lista de Posts:
```
/posts/:postId
```
Substitua :postId pelo Id do post que deseja atualizar e voilà!

#### Rotas DELETE
##### Obter lista de Serviços:
```
/servicos/:servicoId
```
Substitua :servicoId pelo Id do serviço que deseja deletar e voilà!

##### Obter lista de Integrantes da Equipe:
```
/integranteequipe/:integranteId
```
Substitua :integranteId pelo Id do integrante da equipe que deseja deletar e voilà!
##### Obter lista de Posts:
```
/posts/:postId
```
Substitua :postId pelo Id do post que deseja deletar e voilà!



