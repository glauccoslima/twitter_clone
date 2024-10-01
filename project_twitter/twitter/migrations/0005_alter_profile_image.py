# Generated by Django 5.1.1 on 2024-09-29 03:18

from django.db import migrations, models
from project_twitter.twitter.models.profile import validate_image  # Importa o validador de imagem personalizado


class Migration(migrations.Migration):

    dependencies = [
        # Dependência da migração anterior que altera o campo "image" no modelo "Profile"
        ("twitter", "0004_alter_profile_image"),
    ]

    operations = [
        # Altera o campo "image" no modelo "Profile"
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="default.png",  # Define a imagem padrão para perfis
                upload_to="",  # Define o diretório de upload como vazio (pode ser configurado posteriormente)
                validators=[validate_image],  # Adiciona um validador de imagem personalizado
            ),
        ),
    ]
