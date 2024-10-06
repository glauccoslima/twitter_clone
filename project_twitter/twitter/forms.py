# twitter/forms.py

from django import forms  # Importa o módulo forms do Django para criar formulários
from django.contrib.auth.forms import UserCreationForm  # Importa o formulário de criação de usuário padrão do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from .models import Post, Profile, Comment  # Importa os modelos Post, Profile e Comment
import re  # Importa o módulo regex para validação de senha

# Formulário de registro de usuário
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Obrigatório. Insira seu nome.'
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Obrigatório. Insira um email válido.'
    )

    class Meta:
        model = User  # Define o modelo associado ao formulário
        fields = ["first_name", "username", "email", "password1", "password2"]  # Campos que serão exibidos no formulário

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Verifica o comprimento da senha
        if len(password) < 8 or len(password) > 30:
            raise forms.ValidationError('A senha deve ter entre 8 a 30 caracteres.')
        # Verifica a complexidade da senha
        if not re.search(r'[A-Za-z]', password):
            raise forms.ValidationError('A senha deve conter pelo menos uma letra.')
        if not re.search(r'\d', password):
            raise forms.ValidationError('A senha deve conter pelo menos um número.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError('A senha deve conter pelo menos um caractere especial.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'As senhas não coincidem.')

# Formulário para criar um post
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Exclui o usuário atual da verificação para permitir que ele mantenha seu nome de usuário
        if User.objects.filter(username__iexact=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username

# Formulário para atualizar o perfil
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Define o modelo associado ao formulário
        fields = ["image", "bio"]  # Campos que serão exibidos no formulário

# Formulário para adicionar um comentário
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
