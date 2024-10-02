# twitter/forms.py

from django import forms  # Importa o módulo forms do Django para criar formulários
from django.contrib.auth.forms import UserCreationForm  # Importa o formulário de criação de usuário padrão do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from .models import Post, Profile, Comment  # Importa os modelos Post, Profile e Comment

# Formulário de registro de usuário
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Campo de email adicional

    class Meta:
        model = User  # Define o modelo associado ao formulário
        fields = ["first_name", "username", "email", "password1", "password2"]  # Campos que serão exibidos no formulário

    def clean_email(self):
        email = self.cleaned_data.get('email')  # Obtém o email do formulário
        if User.objects.filter(email=email).exists():  # Verifica se o email já está em uso
            raise forms.ValidationError("Email já está em uso.")  # Lança um erro de validação se o email já estiver em uso
        return email  # Retorna o email validado

# Formulário para criar um post (tweet)
class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control w-100",  # Classe CSS para estilização
                "id": "contentsBox",  # ID do campo de texto
                "rows": "3",  # Número de linhas do campo de texto
                "placeholder": "O que está pensando?",  # Placeholder do campo de texto
            }
        )
    )

    class Meta:
        model = Post  # Define o modelo associado ao formulário
        fields = ["content"]  # Campos que serão exibidos no formulário

# Formulário para atualizar o usuário
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  # Define o modelo associado ao formulário
        fields = ["first_name", "username"]  # Campos que serão exibidos no formulário

# Formulário para atualizar o perfil
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Define o modelo associado ao formulário
        fields = ["image", "bio"]  # Campos que serão exibidos no formulário

# Novo formulário para adicionar um comentário
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control w-100",  # Classe CSS para estilização
                "id": "commentBox",  # ID do campo de texto
                "rows": "2",  # Número de linhas do campo de texto
                "placeholder": "Adicione um comentário...",  # Placeholder do campo de texto
            }
        )
    )

    class Meta:
        model = Comment  # Define o modelo associado ao formulário
        fields = ["content"]  # Campos que serão exibidos no formulário
