# twitter/views.py

from django.shortcuts import render, redirect, get_object_or_404  # Importa funções utilitárias do Django
from .models import Profile, Post, Relationship, Like  # Importa os modelos Profile, Post, Relationship e Like
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm, CommentForm  # Importa os formulários personalizados
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from django.contrib.auth.decorators import login_required  # Importa o decorador login_required para proteger views
from django.contrib import messages  # Importa o módulo de mensagens do Django para feedback ao usuário
from django.db import IntegrityError, transaction  # Importa módulos para controle de transações e tratamento de erros

# View para a página inicial, requer login
@login_required
def home(request):
    posts = Post.objects.all().order_by('-timestamp')  # Obtém todos os posts ordenados por timestamp decrescente

    if request.method == "POST":
        form = PostForm(request.POST)  # Cria uma instância do formulário com os dados do POST
        if form.is_valid():
            post = form.save(commit=False)  # Cria um objeto Post sem salvar no banco de dados ainda
            post.user = request.user  # Define o usuário do post como o usuário logado
            post.save()  # Salva o post no banco de dados
            messages.success(request, "Tweet publicado com sucesso!")  # Adiciona uma mensagem de sucesso
            return redirect("home")  # Redireciona para a página inicial
    else:
        form = PostForm()  # Cria uma instância vazia do formulário

    comment_form = CommentForm()  # Cria uma instância vazia do formulário de comentários
    context = {"posts": posts, "form": form, "comment_form": comment_form}  # Contexto para renderização do template
    return render(request, "twitter/newsfeed.html", context)  # Renderiza o template com o contexto

# View para registro de novos usuários
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # Cria uma instância do formulário com os dados do POST
        if form.is_valid():
            try:
                with transaction.atomic():  # Inicia uma transação atômica
                    form.save()  # Salva o novo usuário no banco de dados
                messages.success(request, "Conta criada com sucesso! Você já pode fazer login.")  # Adiciona uma mensagem de sucesso
                return redirect("login")  # Redireciona para a página de login
            except IntegrityError:
                form.add_error(None, "Ocorreu um erro ao criar a conta. Por favor, tente novamente.")  # Adiciona uma mensagem de erro ao formulário
    else:
        form = UserRegisterForm()  # Cria uma instância vazia do formulário

    context = {"form": form}  # Contexto para renderização do template
    return render(request, "twitter/register.html", context)  # Renderiza o template com o contexto

# View para deletar um post
@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)  # Obtém o post ou retorna 404 se não encontrado
    post.delete()  # Deleta o post
    messages.success(request, "Tweet deletado com sucesso!")  # Adiciona uma mensagem de sucesso
    return redirect("home")  # Redireciona para a página inicial

# View para exibir o perfil de um usuário
def profile(request, username):
    user = get_object_or_404(User, username=username)  # Obtém o usuário ou retorna 404 se não encontrado
    posts = user.posts.all().order_by('-timestamp')  # Obtém todos os posts do usuário ordenados por timestamp decrescente
    user_profile = get_object_or_404(Profile, user=user)  # Obtém o perfil do usuário ou retorna 404 se não encontrado
    is_following = False
    if request.user.is_authenticated:
        is_following = Relationship.objects.filter(from_user=request.user, to_user=user).exists()  # Verifica se o usuário logado está seguindo o usuário do perfil
    context = {
        "user_profile": user,
        "profile": user_profile,
        "posts": posts,
        "is_following": is_following
    }
    return render(request, "twitter/profile.html", context)  # Renderiza o template com o contexto

# View para editar o perfil do usuário, requer login
@login_required
def editar(request):
    user = request.user  # Obtém o usuário logado
    user_profile, _ = Profile.objects.get_or_create(user=user)  # Obtém ou cria o perfil do usuário

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=user)  # Cria uma instância do formulário com os dados do POST e o usuário logado
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)  # Cria uma instância do formulário com os dados do POST e os arquivos enviados

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  # Salva as alterações no usuário
            p_form.save()  # Salva as alterações no perfil
            messages.success(request, "Seu perfil foi atualizado com sucesso!")  # Adiciona uma mensagem de sucesso
            return redirect("editar")  # Redireciona de volta para a página de edição
    else:
        u_form = UserUpdateForm(instance=user)  # Cria uma instância do formulário com os dados do usuário logado
        p_form = ProfileUpdateForm(instance=user_profile)  # Cria uma instância do formulário com os dados do perfil do usuário

    context = {"u_form": u_form, "p_form": p_form}  # Contexto para renderização do template
    return render(request, "twitter/editar.html", context)  # Renderiza o template com o contexto

# View para seguir um usuário, requer login
@login_required
def follow(request, username):
    current_user = request.user  # Obtém o usuário logado
    to_user = get_object_or_404(User, username=username)  # Obtém o usuário a ser seguido ou retorna 404 se não encontrado
    if current_user != to_user:
        Relationship.objects.get_or_create(from_user=current_user, to_user=to_user)  # Cria um relacionamento de seguir se não existir
        messages.success(request, f"Você está seguindo {to_user.username}.")  # Adiciona uma mensagem de sucesso
    return redirect("profile", username=username)  # Redireciona para o perfil do usuário seguido

# View para deixar de seguir um usuário, requer login
@login_required
def unfollow(request, username):
    current_user = request.user  # Obtém o usuário logado
    to_user = get_object_or_404(User, username=username)  # Obtém o usuário a ser deixado de seguir ou retorna 404 se não encontrado
    Relationship.objects.filter(from_user=current_user, to_user=to_user).delete()  # Deleta o relacionamento de seguir
    messages.success(request, f"Você deixou de seguir {to_user.username}.")  # Adiciona uma mensagem de sucesso
    return redirect("profile", username=username)  # Redireciona para o perfil do usuário deixado de seguir

# View para adicionar comentários a um post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Obtém o post ou retorna 404 se não encontrado

    if request.method == "POST":
        form = CommentForm(request.POST)  # Cria uma instância do formulário com os dados do POST
        if form.is_valid():
            comment = form.save(commit=False)  # Cria um objeto Comment sem salvar no banco de dados ainda
            comment.post = post  # Define o post do comentário
            comment.user = request.user  # Define o usuário do comentário como o usuário logado
            comment.save()  # Salva o comentário no banco de dados
            messages.success(request, "Comentário adicionado com sucesso!")  # Adiciona uma mensagem de sucesso
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CommentForm()  # Cria uma instância vazia do formulário

    context = {"form": form, "post": post}  # Contexto para renderização do template
    return render(request, "twitter/add_comment.html", context)  # Renderiza o template com o contexto

# View para curtir ou descurtir um post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Obtém o post ou retorna 404 se não encontrado
    like, created = Like.objects.get_or_create(post=post, user=request.user)  # Obtém ou cria um objeto Like
    if not created:
        like.delete()  # Deleta o like se já existir
        messages.success(request, "Você descurtiu o tweet.")  # Adiciona uma mensagem de sucesso
    else:
        messages.success(request, "Você curtiu o tweet.")  # Adiciona uma mensagem de sucesso
    return redirect('home')  # Redireciona para a página inicial

# View personalizada para erro 404
# skipcq: PYL-W0613
def custom_404(request, exception):
    return render(request, 'twitter/404.html', status=404)
