# twitter/admin.py

from django.contrib import admin  # Importa o módulo admin do Django para registrar os modelos no admin site
from .models import Profile, Post, Relationship, Comment, Like  # Importa os modelos Profile, Post, Relationship, Comment e Like

# Registra o modelo Profile no admin site para que possa ser gerenciado através da interface administrativa do Django
admin.site.register(Profile)

# Registra o modelo Post no admin site para que possa ser gerenciado através da interface administrativa do Django
admin.site.register(Post)

# Registra o modelo Relationship no admin site para que possa ser gerenciado através da interface administrativa do Django
admin.site.register(Relationship)

# Registra o modelo Comment no admin site para que possa ser gerenciado através da interface administrativa do Django
admin.site.register(Comment)  # Registrado

# Registra o modelo Like no admin site para que possa ser gerenciado através da interface administrativa do Django
admin.site.register(Like)  # Registrado
