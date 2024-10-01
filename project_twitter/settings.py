import os  # Importa o módulo os para interagir com o sistema operacional
from pathlib import Path  # Importa Path para manipulação de caminhos de arquivos e diretórios

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança e chave secreta
SECRET_KEY = "django-insecure-6=w3+g1o@=@rk$uxak18sr%ic#cqr^ld3a*)0+@zbv2!rrn167"  # Chave secreta para criptografia e segurança
# skipcq: PY-S0900
DEBUG = True  # Define se o modo de depuração está ativado
ALLOWED_HOSTS = ['127.0.0.1', 'ebac-bookstore-api-glaucco.herokuapp.com', '.herokuapp.com']  # Hosts permitidos para acessar o projeto

# Aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",  # Aplicação de administração do Django
    "django.contrib.auth",  # Aplicação de autenticação do Django
    "django.contrib.contenttypes",  # Aplicação de tipos de conteúdo do Django
    "django.contrib.sessions",  # Aplicação de sessões do Django
    "django.contrib.messages",  # Aplicação de mensagens do Django
    "django.contrib.staticfiles",  # Aplicação de arquivos estáticos do Django
    "django_extensions",  # Extensões adicionais para o Django
    'project_twitter.twitter.apps.TwitterConfig',  # Configuração do aplicativo Twitter
    "rest_framework",  # Framework para construção de APIs RESTful
   # "debug_toolbar",  # Ferramenta de depuração para Django
    "rest_framework.authtoken",  # Autenticação baseada em token para APIs REST
    "django.contrib.humanize",  # Aplicação para formatação de dados humanizada
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Middleware de segurança
    "django.contrib.sessions.middleware.SessionMiddleware",  # Middleware de sessões
    "django.middleware.common.CommonMiddleware",  # Middleware comum
    "django.middleware.csrf.CsrfViewMiddleware",  # Middleware de proteção contra CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Middleware de autenticação
    "django.contrib.messages.middleware.MessageMiddleware",  # Middleware de mensagens
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Middleware de proteção contra clickjacking
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Middleware para servir arquivos estáticos com WhiteNoise
    # "debug_toolbar.middleware.DebugToolbarMiddleware",  # Middleware para Debug Toolbar
]

# Configuração de URLs raiz
ROOT_URLCONF = "project_twitter.urls"

# Configuração de templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Backend de templates do Django
        "DIRS": [os.path.join(BASE_DIR, "twitter", "templates")],  # Diretórios de templates
        "APP_DIRS": True,  # Habilita a busca de templates nos diretórios das aplicações
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # Processador de contexto para depuração
                "django.template.context_processors.request",  # Processador de contexto para requisições
                "django.contrib.auth.context_processors.auth",  # Processador de contexto para autenticação
                "django.contrib.messages.context_processors.messages",  # Processador de contexto para mensagens
            ],
        },
    },
]

# Configuração da aplicação WSGI
WSGI_APPLICATION = "project_twitter.wsgi.application"

# Configuração do banco de dados
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),  # Motor do banco de dados
        "NAME": str(os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3")),  # Nome do banco de dados
        "USER": os.environ.get("SQL_USER", "user"),  # Usuário do banco de dados
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),  # Senha do banco de dados
        "HOST": os.environ.get("SQL_HOST", "localhost"),  # Host do banco de dados
        "PORT": os.environ.get("SQL_PORT", "5432"),  # Porta do banco de dados
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Validador de similaridade de atributos do usuário
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Validador de comprimento mínimo da senha
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Validador de senhas comuns
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Validador de senhas numéricas
    },
]

# Internacionalização
LANGUAGE_CODE = "pt-br"  # Código de idioma
TIME_ZONE = "UTC"  # Fuso horário
USE_I18N = True  # Habilita a internacionalização
USE_L10N = True  # Habilita a formatação local
USE_TZ = True  # Habilita o uso de fuso horário

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuração do Django REST framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# Arquivos estáticos e mídia
STATIC_URL = "/static/"  # URL para arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório raiz para arquivos estáticos

MEDIA_URL = "/media/"  # URL para arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório raiz para arquivos de mídia

# Diretórios estáticos adicionais
if DEBUG:
    STATICFILES_DIRS = [
        # Adicione diretórios adicionais aqui
    ]

# Configurações de login e logout
LOGIN_REDIRECT_URL = '/'  # URL de redirecionamento após login
LOGOUT_REDIRECT_URL = '/login'  # URL de redirecionamento após logout
LOGIN_URL = 'login'  # URL para a página de login
LOGOUT_URL = 'logout'  # URL para a página de logout

# IPs internos permitidos para Debug Toolbar
# if DEBUG:
#    INTERNAL_IPS = [
#        "127.0.0.1",  # IP local
#    ]

# WhiteNoise para compressão e cache de arquivos estáticos
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # Configuração de armazenamento de arquivos estáticos com WhiteNoise
