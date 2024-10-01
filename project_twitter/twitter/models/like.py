from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from .post import Post  # Importa o modelo Post do mesmo pacote

# Define o modelo Like para representar as curtidas nos posts
class Like(models.Model):
    # Chave estrangeira para o modelo Post, com relacionamento de muitos-para-um
    # related_name="post_likes" permite acessar as curtidas de um post com post.post_likes
    # on_delete=models.CASCADE garante que as curtidas sejam deletadas se o post for deletado
    post = models.ForeignKey(Post, related_name="post_likes", on_delete=models.CASCADE)  # Alterado para "post_likes" para evitar conflito

    # Chave estrangeira para o modelo User, com relacionamento de muitos-para-um
    # on_delete=models.CASCADE garante que as curtidas sejam deletadas se o usuário for deletado
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Campo de data e hora que armazena o timestamp de criação da curtida
    # auto_now_add=True define automaticamente o valor do campo para a data e hora atuais quando a curtida é criada
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que um usuário possa curtir um post apenas uma vez
        unique_together = ('post', 'user')

    def __str__(self):
        # Retorna uma representação em string da curtida, mostrando o nome de usuário e os primeiros 20 caracteres do conteúdo do post
        return f"{self.user.username} likes {self.post.content[:20]}"
