# twitter/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

# Lista de URLs que mapeiam para as views correspondentes
urlpatterns = [
    # URL para a página inicial
    path("", views.home, name="home"),

    # URL para a página de registro de novos usuários
    path("register/", views.register, name="register"),

    # URL para logout, utilizando a view padrão do Django
    path("logout/", LogoutView.as_view(), name="logout"),

    # URL para deletar um post específico, identificado pelo ID do post
    path("delete/<int:post_id>/", views.delete, name="delete"),

    # URL para visualizar o perfil de um usuário específico, identificado pelo nome de usuário
    path("profile/<str:username>/", views.profile, name="profile"),

    # URL para editar informações do usuário
    path("editar/", views.editar, name="editar"),

    # URL para seguir um usuário específico, identificado pelo nome de usuário
    path("follow/<str:username>/", views.follow, name="follow"),

    # URL para deixar de seguir um usuário específico, identificado pelo nome de usuário
    path("unfollow/<str:username>/", views.unfollow, name="unfollow"),

    # URL para adicionar um comentário a um post específico, identificado pelo ID do post
    path("add_comment/<int:post_id>/", views.add_comment, name="add_comment"),

    # URL para curtir um post específico, identificado pelo ID do post
    path("like/<int:post_id>/", views.like_post, name="like_post"),
]

# Adiciona URLs para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
