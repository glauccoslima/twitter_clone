# manage.py

"""Django's command-line utility for administrative tasks."""
import os  # Importa o módulo os para interagir com o sistema operacional
import sys  # Importa o módulo sys para manipulação de argumentos e caminho do sistema
from pathlib import Path  # Importa Path para manipulação de caminhos de arquivos e diretórios

def main():
    """Run administrative tasks."""
    # Definir o caminho base do projeto e garantir que o diretório project_twitter seja incluído no sys.path
    BASE_DIR = Path(__file__).resolve().parent  # Define o diretório base do projeto

    # Verificar se a pasta 'media' existe e, se não, criá-la
    media_dir = BASE_DIR / 'media'  # Define o caminho para o diretório 'media'
    if not media_dir.exists():  # Verifica se o diretório 'media' não existe
        media_dir.mkdir()  # Cria o diretório 'media'

    # Define a variável de ambiente DJANGO_SETTINGS_MODULE com o caminho para o arquivo de configurações do projeto
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_twitter.settings")
    try:
        # Importa a função execute_from_command_line do Django para executar comandos administrativos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Lança um erro se o Django não puder ser importado, sugerindo possíveis causas
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Executa o comando administrativo passado como argumento na linha de comando
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()  # Chama a função main se este arquivo for executado como script principal
