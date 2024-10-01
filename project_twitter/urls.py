from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls import handler404
from project_twitter.twitter import views as twitter_views  # Importa twitter_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Rotas de autenticação padrão
    path('', include('project_twitter.twitter.urls')),  # Suas rotas principais, sem 'login/' duplicado
    path('', RedirectView.as_view(url='/login', permanent=False)),  # Redireciona para login
]

handler404 = twitter_views.custom_404

# Adiciona rotas adicionais em modo de depuração
# if settings.DEBUG:
#    import debug_toolbar  # Importa o debug_toolbar para depuração
#    urlpatterns += [
#        path('__debug__/', include(debug_toolbar.urls)),  # Rota para a Debug Toolbar
#    ]
#    # Serve arquivos de mídia durante o desenvolvimento
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    # Serve arquivos estáticos durante o desenvolvimento
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
