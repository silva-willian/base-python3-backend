# API Flask com Swagger

Este é um projeto base para criar uma API simples usando Flask

## Pré-requisitos

- Python 3 instalado
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório: git clone https://github.com/seu-usuario/nome-do-projeto.git
2. Navegue até o diretório do projeto
3. Instale as dependências do projeto: pip3 install -r requirements.txt

## Executando o Projeto

Para executar o projeto, você pode usar o comando:


O aplicativo estará disponível em `http://localhost:5000`.


## Testando a API

Você pode executar os testes unitários do projeto usando o comando: python3 -m unittest test_api.py


## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `api.py`: Arquivo principal que define a aplicação Flask.
- `api_routes.py`: Contém as definições das rotas da API.
- `api_healthcheck.py`: Define a rota para o healthcheck da aplicação.
- `logger.py`: Configuração do logger da aplicação.
- `test_api.py`: Arquivo com os testes unitários para a API.
- `requirements.txt`: Lista de dependências do projeto.
