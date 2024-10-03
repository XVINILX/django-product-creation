FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

RUN python manage.py makemigrations || echo "Migrations skipped as database may not be available."
RUN python manage.py migrate || echo "Migrations skipped as database may not be available."

# Expõe a porta do servidor
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
