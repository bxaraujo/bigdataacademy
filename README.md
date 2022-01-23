# Desafio Deloitte + Big Data Academy 
## DELOITTE BIG DATA - CASE TÉCNICO

Para realizar este case técnico, optei por seguir o desafio do BACKEND, visto que tenho mais conhecimento e prática nesta área.


## Tecnologias utilizadas

* Python
* Django + Django Rest Framework
* drf_yasg
* QLite
* PostgreSQL
* Heroku

### Python

Optei por utilizar o python para realizar o desafio por ter mais experiência com esta linguagem

### Django + Django Rest Framework

A utilização do Django como framework para desenvolvimento da aplicação WEB e Django Rest Framework devido as particularidades do desafio em solicitar uma API Rest.
O Django com o django rest framework nos trás uma grande quantidade de ferramentas que facilitam o desenvolvimento de REST APIs como serializadores, modelos e views, assim como banco de dado e servidor integrado para ambiente de desenvolvimento. 
Além disso também possui facilidades para autenticação e permissões, assim como painel administrativo de setup facilitado.

### drf_yasg

Para documentar a API escolhi utilizar o drf_yasg, pacote muito útil que documenta a REST API desenvolvida com o django rest framework nos formatos mais utilizados no mercado como OPENAPI e REDOC.

### SQLite

Banco de dados relacional utilizado para ambiente de desenvolvimento e também para o commit no GitHub, visto que sua estrutura simples em formato de arquivo é de fácil utilização e possível de rodar localmente.

### PostgreSQL

Banco de dados relacional, bastante robusto e confiável, utilizado para o ambiente de produção.

### Heroku

Decidi utilizar o heroku como ferramenta e PaaS para deploy da API em produção.



## Setup do ambiente de teste e desenvolvimento

### Instalar requirements em ambiente que utilize 
```
pip install -r requirements.txt
```

## Utilização

### Login e autenticação simples

Acessar a rota:
```
/admin/
```
Para administrar o conteúdo via painel de gerenciamento, utilizar o usuário **admin** e a senha **admin** . 
Usuário: admin
Senha: admin

## Documentação OPENAPI, REDOC e SWAGGER

/swagger/
/swagger.json
/swagger.yaml

/swagger/?format=openapi

http://127.0.0.1:9999/redoc/

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
/equipe/
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
##### Criar novo Integrante da Equipe:
```
/equipe/
```
##### Criar novo Post:
```
/posts/
```

#### Rotas PUT
##### Atualizar serviço específico:
```
/servicos/:servicoId
```
Substitua :servicoId pelo Id do serviço que deseja atualizar e voilà!

##### Obter lista de Integrantes da Equipe:
```
/equipe/:integranteId
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
/equipe/:integranteId
```
Substitua :integranteId pelo Id do integrante da equipe que deseja deletar e voilà!
##### Obter lista de Posts:
```
/posts/:postId
```
Substitua :postId pelo Id do post que deseja deletar e voilà!



