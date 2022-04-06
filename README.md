# Copia dados de um excel para um banco de dados.

Para facilizar o processo vou utlizar **ORM** do **django**.

```console
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Após isso teremos o banco de dados **sqlite** chamado **db.sqlite3**

A o aqruivo excel que usaremos de teste chama-se **Planilha.xlsx** e pode ser encontrado no diretorio raiz do projeto. Para ler o excel foi usado o módulo
**openpyxl**.

Para transferir os dados do excel para o db.sqlite3:

```console
python excel_para_banco.py
```

Agora os dados foram transferidos da **Planilha.xlsx** para a tabela **core_tabela** do sqlite3.