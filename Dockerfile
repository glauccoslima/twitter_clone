# `python-base` configura todas as nossas variáveis de ambiente compartilhadas
FROM python:3.11.10-slim AS python-base

# Configurações do Python, Impede que o Python faça buffering da saída, Impede que o Python crie arquivos .pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Configurações do pip, Desativa o cache do pip, Desativa a verificação de versão do pip, Define o tempo limite padrão do pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Configurações do Poetry, Define a versão do Poetry, Define o local de instalação do Poetry, Faz o Poetry criar o ambiente virtual na raiz do projeto, Desativa perguntas interativas do Poetry
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # Caminhos de configuração do Python, Local onde os requisitos e o ambiente virtual serão armazenados, Caminho do ambiente virtual
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona o Poetry e o ambiente virtual ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Atualiza os pacotes e instala dependências necessárias para o Poetry, Python, Git e para compilar dependências do Python
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry - respeita as variáveis $POETRY_VERSION e $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# Define o diretório de trabalho para o caminho de configuração do Python
WORKDIR $PYSETUP_PATH

# Copia os arquivos de requisitos do projeto para garantir que serão armazenados em cache
COPY poetry.lock pyproject.toml ./

# Instala as dependências de runtime e desenvolvimento de uma só vez
RUN poetry install

# Define o diretório de trabalho para o diretório da aplicação
WORKDIR /app

# Copia todo o conteúdo do projeto para o diretório da aplicação
COPY . /app/

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Adiciona um healthcheck para verificar se o servidor Django está rodando
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
