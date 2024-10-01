from django.apps import AppConfig  # Importa a classe AppConfig do Django para configuração do aplicativo

# Define a configuração do aplicativo Twitter
class TwitterConfig(AppConfig):
    # Define o campo padrão de chave primária como BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo como 'project_twitter.twitter'
    name = 'project_twitter.twitter'

    # Método ready é chamado quando o aplicativo está pronto para ser usado
    # skipcq: PYL-R0201
    def ready(self):
        # Importação relativa para evitar problemas de resolução de caminhos
        # Importa o módulo signals para conectar os sinais definidos no aplicativo
        # skipcq: PY-W2000
        from . import signals
