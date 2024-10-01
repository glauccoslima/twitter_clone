from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from .post import Post  # Importa o modelo Post do mesmo pacote

# Define o modelo Comment para representar os comentários nos posts
class Comment(models.Model):
    # Chave estrangeira para o modelo Post, com relacionamento de muitos-para-um
    # related_name="comments" permite acessar os comentários de um post com post.comments
    # on_delete=models.CASCADE garante que os comentários sejam deletados se o post for deletado
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    # Chave estrangeira para o modelo User, com relacionamento de muitos-para-um
    # on_delete=models.CASCADE garante que os comentários sejam deletados se o usuário for deletado
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Campo de texto para o conteúdo do comentário
    content = models.TextField()

    # Campo de data e hora que armazena o timestamp de criação do comentário
    # auto_now_add=True define automaticamente o valor do campo para a data e hora atuais quando o comentário é criado
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Define a ordenação padrão dos comentários por timestamp em ordem decrescente
        ordering = ["-timestamp"]

    def __str__(self):
        # Retorna uma representação em string do comentário, mostrando o nome de usuário e o conteúdo
        return f"{self.user.username}: {self.content}"
