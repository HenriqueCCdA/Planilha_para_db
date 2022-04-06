# Copia dados de um arquivo xlsx para um banco de dados.

Para facilizar o processo vou utlizar **ORM** do **django**.

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Agora temos a tabela **core_tabela** no banco de dados. Esta tabela irá recever os dados do arquivo excel.

O aqruivo excel que usaremos de teste chama-se **Planilha.xlsx**. Ele pode ser encontrado no diretorio raiz do projeto. Para ler o excel foi usado o módulo **openpyxl**.

Para transferir os dados do excel para o **db.sqlite3** basta executar o arquivo **excel_para_banco.py**:

```console
python excel_para_banco.py
```

Agora os dados foram transferidos da **Planilha.xlsx** para a tabela **core_tabela**.
