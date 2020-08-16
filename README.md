# NavedexAPI

Para o desenvolvimento desta API, foram utilizados Django, Django REST Framework e PostgreSQL.

Siga as seguintes instruções para instalação do projeto:

2. Na pasta criada após clonar o projeto, execute o seguinte comando:
``pip install -r requirements.txt``

3. Em seguida, acesse o arquivo **settings.py**, localizado na pasta, e altere a seção **DATABASES** de acordo com as suas configurações de banco de dados:
``DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <nome_do_seu_bd>,
        'USER': <seu_user>,
        'PASSWORD': <sua_senha>,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}``

4. Agora rode o seguinte comando para aplicar as migrações no seu banco de dados:
``python manage.py migrate``

5. Por último, para executar a API, execute o seguinte comando:
``python manage.py runserver``

## Teste da API

A URLs da API e o seus respectivos métodos são as seguintes:

Método   | URL    
--------- | ------ 
GET, POST | /project
GET, PUT, DELETE | /project/<id_project>
GET, POST | /naver
GET, PUT, DELETE | /naver/<id_naver>
POST | /user/register
POST | /user/token , /user/token/refresh

Já o JSON utilizado para passar atributos de objetos a serem cadastrados/atualizados nas requisições possui a seguinte estrutura:
### User
``
{
 "email": "email@email.com",
 "password": "senha_do_usuario"
}
``

### Project
``
{
  "name": "Nome do projeto",
  "navers": [<id_naver>]
}
``

### Naver
``
{
  "name": "Nome do naver",
  "projects": [<id_project>],
  "birthdate": "2001-09-20",
  "admission_date": "2020-01-20",
  "job_role": "Dev"
}
``
O teste da API deve ser feito da seguinte forma:
1. Cadastre um usurio com a URL /user/register , com o método POST, passando no Body da requisição o email e senha desejados.
2. Logue com seu usuário e receba um token para realizar os outros testes através da url /user/token , com o método POST. O token dura 24h e deve ser passado no através do cabeçalho Authorization dessa maneira: Bearer <token>
3. Crie um projeto com a URL /project usando o método POST
4. Em seguida, crie um naver com a URL /naver, usando o método POST
  
**OBS.:** Os passos 3 e 4 podem ser invertidos. O que importa é que haja um objeto primeiro para que o outro possa ser criado :)

5. Com navers e projetos cadastrados, você pode visualizar suas listagens ou objetos individualmente. Durante as consultas gerais, você pode utilizar filtros:
Filtro   | Descrição
--------- | ------ 
/project?name=<nome_projeto> | Filtra pelo nome do projeto
/naver?name=<nome_naver> | Filtra pelo nome do naver
/naver?job_role=<nome_funcao> | Filtra pela função do naver
/naver?initial_date=<data_inicio>?final_date=<data_fim> | Filtra pela data de admissão dentro do range descrito

Além disso, você pode editar e deletar os objetos de acordo com as URLs e métodos descritos anteriormente.

##Dificuldades
Durante o desenvolvimento dos projeto, tive dificuldades com a resposta das requisições, ao editar os campos do JSON. Portanto, alguns campos como o de user_id estão aparecendo nos objetos naver e project, e a lista de projetos não aparece corretamente para o naver.
