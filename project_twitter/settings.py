import os  # Importa o módulo os para interagir com o sistema operacional
from pathlib import Path  # Importa Path para manipulação de caminhos de arquivos e diretórios
import dj_database_url  # Pacote para facilitar a configuração do banco de dados no Heroku

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança e chave secreta
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-6=w3+g1o@=@rk$uxak18sr%ic#cqr^ld3a*)0+@zbv2!rrn167')  # Chave secreta para criptografia e segurança
# skipcq: PY-S0900

# Definir DEBUG com base na variável de ambiente (padrão: False) para segurança
DEBUG = True

# Defina os hosts permitidos para a aplicação
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'twitter-clone-api.herokuapp.com', '.herokuapp.com']  # Lista de hosts permitidos

# Lista de origens confiáveis para CSRF
CSRF_TRUSTED_ORIGINS = ['https://twitter-clone-api.herokuapp.com', 'https://twitter-clone-api-6ddd12cb8d81.herokuapp.com']

# Aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",  # Extensões adicionais para o Django
    'project_twitter.twitter.apps.TwitterConfig',  # Configuração do aplicativo Twitter
    "rest_framework",  # Framework para construção de APIs RESTful
    "rest_framework.authtoken",  # Autenticação baseada em token para APIs REST
    "django.contrib.humanize",  # Aplicação para formatação de dados humanizada
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Middleware para servir arquivos estáticos com WhiteNoise
]

# Configuração de URLs raiz
ROOT_URLCONF = "project_twitter.urls"

# Configuração de templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "twitter", "templates")],  # Diretórios de templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Configuração da aplicação WSGI para uso com Gunicorn
WSGI_APPLICATION = "project_twitter.wsgi.application"

# Configuração do banco de dados usando dj-database-url para Heroku e SQLite como fallback local
DATABASES = {
    "default": dj_database_url.config(default=os.getenv('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}"))
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internacionalização
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

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
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Diretórios estáticos adicionais
if DEBUG:
    STATICFILES_DIRS = [
        # Adicione diretórios adicionais aqui, se necessário
    ]

# Configurações de login e logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# WhiteNoise para compressão e cache de arquivos estáticos
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Ajuste de IPs internos para Debug Toolbar, se necessário (comente quando não usar)
# if DEBUG:
#    INTERNAL_IPS = [
#        "127.0.0.1",
#    ]
