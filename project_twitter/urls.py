# project_twitter/urls.py

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls import handler404
from django.contrib.auth.views import LoginView, LogoutView
from project_twitter.twitter import views as twitter_views

# Lista de URLs que mapeiam para as views correspondentes
urlpatterns = [
    # URL para acessar a interface de administração do Django
    path('admin/', admin.site.urls),

    # Inclui as URLs de autenticação padrão do Django (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Inclui as URLs do aplicativo Twitter
    path('twitter/', include('project_twitter.twitter.urls')),

    # URL para a página de login, utilizando a view padrão do Django com um template customizado
    path('login/', LoginView.as_view(template_name="twitter/login.html"), name='login'),

    # Redireciona a URL raiz para /twitter/
    path('', RedirectView.as_view(url='/twitter/', permanent=False)),
]

# Define uma view customizada para tratar erros 404 (página não encontrada)
handler404 = twitter_views.custom_404
