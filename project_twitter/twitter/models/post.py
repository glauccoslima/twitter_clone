from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from django.utils import timezone  # Importa o módulo timezone para manipulação de datas e horas

# Define o modelo Post para representar os posts dos usuários
class Post(models.Model):
    # Campo ID com auto incremento, usado como chave primária
    id = models.BigAutoField(primary_key=True)

    # Campo de data e hora que armazena o timestamp de criação do post
    # default=timezone.now define automaticamente o valor do campo para a data e hora atuais quando o post é criado
    timestamp = models.DateTimeField(default=timezone.now)

    # Campo de texto para o conteúdo do post
    content = models.TextField()

    # Chave estrangeira para o modelo User, com relacionamento de muitos-para-um
    # related_name="posts" permite acessar os posts de um usuário com user.posts
    # on_delete=models.CASCADE garante que os posts sejam deletados se o usuário for deletado
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    # Campo de relacionamento muitos-para-muitos com o modelo User, representando as curtidas
    # related_name='liked_posts' permite acessar os posts curtidos por um usuário com user.liked_posts
    # through="Like" especifica o modelo intermediário Like para o relacionamento M2M
    # blank=True permite que o campo seja opcional
    likes = models.ManyToManyField(User, related_name='liked_posts', through="Like", blank=True)

    class Meta:
        # Define a ordenação padrão dos posts por timestamp em ordem decrescente (do mais recente para o mais antigo)
        ordering = ["-timestamp"]

    # Método para retornar o total de curtidas de um post
    def total_likes(self):
        return self.likes.count()  # Retorna o total de curtidas

    # Método para retornar uma representação em string do post
    def __str__(self):
        return self.content  # Retorna o conteúdo do post como sua representação em string
