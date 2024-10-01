# twitter/urls.py

from django.urls import path  # Importa a função path para definir as rotas
from . import views  # Importa as views do aplicativo atual
from django.contrib.auth.views import LoginView, LogoutView  # Importa as views de login e logout padrão do Django
from django.conf import settings  # Importa as configurações do projeto
from django.conf.urls.static import static  # Importa a função static para servir arquivos estáticos em modo de desenvolvimento

# Define as rotas do aplicativo
urlpatterns = [
    path("", views.home, name="home"),  # Rota para a página inicial
    path("register/", views.register, name="register"),  # Rota para a página de registro
    path("login/", LoginView.as_view(template_name="twitter/login.html"), name="login"),  # Rota para a página de login
    path("logout/", LogoutView.as_view(), name="logout"),  # Rota para logout
    path("delete/<int:post_id>/", views.delete, name="delete"),  # Rota para deletar um post
    path("profile/<str:username>/", views.profile, name="profile"),  # Rota para visualizar o perfil de um usuário
    path("editar/", views.editar, name="editar"),  # Rota para editar o perfil do usuário
    path("follow/<str:username>/", views.follow, name="follow"),  # Rota para seguir um usuário
    path("unfollow/<str:username>/", views.unfollow, name="unfollow"),  # Rota para deixar de seguir um usuário

    # Nova rota para adicionar comentários
    path("add_comment/<int:post_id>/", views.add_comment, name="add_comment"),  # Rota para adicionar um comentário a um post

    # Nova rota para curtir um post
    path("like/<int:post_id>/", views.like_post, name="like_post"),  # Rota para curtir um post
]

# Adicionando rotas de mídia para servir arquivos em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve arquivos de mídia durante o desenvolvimento
