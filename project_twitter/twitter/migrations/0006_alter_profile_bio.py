# Generated by Django 5.1.1 on 2024-10-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.CharField(default="Ola, twitter!", max_length=100),
        ),
    ]
