from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

# Define a classe Relationship que estende models.Model
class Relationship(models.Model):
    # Campo id como BigAutoField para chave primária
    id = models.BigAutoField(primary_key=True)

    # Campo from_user como ForeignKey relacionado ao modelo User do Django
    # related_name='relationships' permite acessar os relacionamentos de um usuário através de user.relationships
    # Se o usuário for deletado, todos os relacionamentos associados também serão deletados (CASCADE)
    from_user = models.ForeignKey(
        User, related_name="relationships", on_delete=models.CASCADE
    )

    # Campo to_user como ForeignKey relacionado ao modelo User do Django
    # related_name='related_to' permite acessar os relacionamentos onde o usuário é o destinatário através de user.related_to
    # Se o usuário for deletado, todos os relacionamentos associados também serão deletados (CASCADE)
    to_user = models.ForeignKey(
        User, related_name="related_to", on_delete=models.CASCADE
    )

    # Método __str__ para representação em string do objeto Relationship
    def __str__(self):
        # Retorna uma string representando o relacionamento no formato 'from_user to to_user'
        return f"{self.from_user} to {self.to_user}"
