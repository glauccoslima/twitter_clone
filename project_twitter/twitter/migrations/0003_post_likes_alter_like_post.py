# Generated by Django 5.1.1 on 2024-09-27 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # Dependência da migração anterior que cria os modelos Comment e Like
        ("twitter", "0002_comment_like"),
        # Dependência do modelo de usuário configurável no settings
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Adiciona o campo "likes" ao modelo "Post"
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True,  # Permite que o campo seja opcional
                related_name="liked_posts",  # Nome da relação reversa para o usuário
                through="twitter.Like",  # Especifica o modelo intermediário "Like"
                to=settings.AUTH_USER_MODEL,  # Relaciona com o modelo de usuário
            ),
        ),
        # Altera o campo "post" no modelo "Like"
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,  # Deleta os likes se o post for deletado
                related_name="post_likes",  # Nome da relação reversa para o post
                to="twitter.post",  # Relaciona com o modelo "Post"
            ),
        ),
    ]
