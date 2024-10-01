# twitter/signals.py

from django.db.models.signals import post_save  # Importa o sinal post_save do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from django.dispatch import receiver  # Importa o decorador receiver para conectar sinais a funções
from .models import Profile  # Importa o modelo Profile

# Função para criar um perfil de usuário automaticamente quando um novo usuário é criado
@receiver(post_save, sender=User)
# skipcq: PYL-W0613
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Verifica se o usuário foi criado
        Profile.objects.create(user=instance)  # Cria um perfil associado ao usuário

# Função para salvar o perfil de usuário automaticamente quando o usuário é salvo
@receiver(post_save, sender=User)
# skipcq: PYL-W0613
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Salva o perfil associado ao usuário
