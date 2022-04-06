# Repositorio que copia dados de um excel para um banco de dados.

Para facilizar o processo vou utlizar o django para cria a tabela atraves da migrações. Para isso basta fazer as migrações com


```console
python manage.py makemigrations
python manage.py migrate
```

Após isso teremos o banco de dados **sqlite** chamado **db.sqlite3**

A o aqruivo excel que usaremos de teste chama-se **Planilha.xlsx** e pode ser encontrado no diretorio raiz do projeto. Para ler o excel foi usado o módulo
**openpyxl**.

Para transferir os dados do excel para o db.sqlite3:

```console
python excel_para_banco.py
```