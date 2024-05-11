# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt /app/
COPY api.py /app/
COPY api_routes.py /app/
COPY api_healthcheck.py /app/
COPY logger.py /app/
COPY test_api.py /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para acessar a aplicação Flask
EXPOSE 5000

# Define o comando padrão para iniciar a aplicação Flask
CMD ["python", "ap9.py"]
