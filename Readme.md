## Teste Sigma - Django Rest


Passo 1: Construir e Rodar os Contêineres
No terminal, navegue até o diretório onde estão seus arquivos Dockerfile e docker-compose.yml, e execute o seguinte comando para construir e iniciar os contêineres:

docker-compose up --build


Passo 5: Executar as Migrações
Após os contêineres estarem rodando, você precisa executar as migrações para criar as tabelas no banco de dados. Em um novo terminal, execute:

docker-compose exec web python manage.py migrate