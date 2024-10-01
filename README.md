# Twitter Clone 🐦

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Componentes Principais](#componentes-principais)
- [Estrutura do Projeto](#estrutura-do-projeto)

## Sobre o Projeto

O **Twitter Clone** é uma aplicação web que simula as principais funcionalidades do Twitter, permitindo que os usuários criem perfis, postem tweets, curtam e comentem em posts. O objetivo é proporcionar uma experiência semelhante ao Twitter, explorando os recursos do Django e outras tecnologias web.

🌐 [**Visite o site!**](/) 👈

## Funcionalidades

- **Cadastro e Autenticação de Usuários**: Os usuários podem se registrar, fazer login e logout.
- **Postagem de Tweets**: É possível criar, visualizar e deletar tweets.
- **Curtidas em Posts**: Implementação do sistema de curtidas em tweets.
- **Comentários em Posts**: Os usuários podem comentar nos tweets.
- **Perfis de Usuário**: Cada usuário possui um perfil com foto, bio e informações pessoais.
- **Integração com API**: A aplicação utiliza Django REST Framework para criar APIs RESTful.

## Tecnologias Utilizadas

- **Django**: Framework web principal utilizado no backend.
- **Django REST Framework**: Para criação de APIs RESTful.
- **PostgreSQL**: Banco de dados relacional utilizado.
- **Docker & Docker Compose**: Para containerização e gerenciamento de serviços.
- **Poetry**: Gerenciador de dependências e ambiente virtual.
- **Pytest**: Para testes automatizados.
- **Pillow**: Para manipulação de imagens (upload de fotos de perfil).
- **Gunicorn**: Servidor WSGI para deploy em produção.
- **Whitenoise**: Para servir arquivos estáticos em produção.
- **HTML/CSS/JavaScript**: Tecnologias web básicas para o frontend.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/glauccoslima/twitter_clone.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd twitter_clone
   ```

3. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` com as configurações necessárias (baseado em `env.dev` se existir).

4. **Inicie os serviços com Docker Compose:**

   ```bash
   docker-compose up -d --build
   ```

   Isso irá construir as imagens Docker e iniciar os containers para o web server e o banco de dados.

5. **Execute migrações e colete arquivos estáticos:**

   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --no-input
   ```

6. **Acesse a aplicação:**

   Abra o navegador e vá para `http://127.0.0.1:8000/` para ver a aplicação em execução.

## Componentes Principais

### Aplicação Django

- **Models**: Definição das entidades principais como `User`, `Post`, `Profile`, `Comment` e `Like`.
- **Views**: Contém a lógica de negócio para manipulação das requisições e respostas.
- **Forms**: Formulários utilizados para registro, login, criação de posts, etc.
- **Templates**: Arquivos HTML que renderizam as páginas do usuário.
- **URLs**: Rotas da aplicação que mapeiam URLs para as views correspondentes.

### APIs RESTful

- Implementação de endpoints utilizando Django REST Framework para interação com dados via API.

### Frontend

- **Templates HTML**: Utilizam Bootstrap para estilização e oferecem uma interface amigável ao usuário.
- **Arquivos estáticos**: CSS, JavaScript e imagens necessários para o frontend.

## Estrutura do Projeto

- `project_twitter/`: Diretório raiz do projeto Django.
  - `settings.py`: Configurações do projeto.
  - `urls.py`: Configurações de URLs raiz.
  - `wsgi.py` e `asgi.py`: Configurações para deploy.
- `twitter/`: Aplicação principal com a lógica do Twitter.
  - `models/`: Contém os modelos de dados (`post.py`, `profile.py`, etc.).
  - `views.py`: Lógica das views.
  - `forms.py`: Formulários da aplicação.
  - `templates/`: Arquivos HTML para renderização.
  - `urls.py`: Rotas específicas da aplicação.
- `media/`: Diretório para uploads de usuários, como fotos de perfil.
- `staticfiles/`: Arquivos estáticos coletados para produção.
- `Dockerfile` e `docker-compose.yml`: Configurações para containerização com Docker.
- `pyproject.toml`: Gerenciamento de dependências com Poetry.
- `requirements.txt`: Lista de dependências (gerado pelo Poetry).
- `manage.py`: Script de gerenciamento do Django.

---
