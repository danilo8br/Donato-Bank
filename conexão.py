# Importando e conectando com o Mysql
import MySQLdb

host = "o host"
user = "seu usario"
password = "sua senha"
db = "nome do banco"
port = "porta" # Example: 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor() # Pegar o resultado

# Selecionado no Banco
def select(fields, tables, where=None): # Campos, tabelas e clausula None

    global c # Resultado

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where

    c.execute(query)

    return c.fetchall() # Retornar a função

# Inserindo no banco

def insert(values, table, fields=None): # Valores, tabelas e campos 

    global c, con # Cursor e conexão

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

values = ["DEFAULT, 'Allan Donato', 'M', '18', '345.765.122-77', 'São Paulo'"]


insert(values, "pessoas")
