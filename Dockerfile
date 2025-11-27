# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Instalar dependências do sistema (opcional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia o código fonte (mantém o layout src/)
COPY src /app/src
COPY tests /app/tests

EXPOSE 5000

# Comando para iniciar a app (módulo Flask)
CMD ["python", "-m", "src.api.app"]
