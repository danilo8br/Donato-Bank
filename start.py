# Importando a bilioteca Mysql
import MySQLdb
# Importando a biblioteca sleep 
from time import sleep

# Dados do seu banco para conectar
host = "o host"
user = "seu usuario"
password = "sua senha"
db = "nome do banco"
port = "porta" # Example: 3306

# Conectando com as variaveis do seu banco
con = MySQLdb.connect(host, user, password, db, port)

# Pegando o resultado
c = con.cursor() #


# Menu de interatividade
def menu():
    print('-=' * 25)

menu()
print('Bem-vindo ao Donato Bank')
sleep(2)
print('Que bom que você escolheu nosso banco!')
sleep(2)
print('Somos o Banco Digital mais Valorizado do Brasil!')
sleep(2)
print('Vamos nessa!!!')
menu()


# Cadastro do usuario
def opcaoUsuario():
    print('-=' * 25)

opcaoUsuario()
nome = str(input('Digite seu nome completo: '))
sleep(0.5)
email = str(input('Digite seu e-mail: '))
sleep(0.5)
senha = str(input('Digite sua senha: '))
sleep(0.5)
sexo = str(input('Digite seu sexo: '))
sleep(0.5)
idade = int(input('Digite sua idade: '))
sleep(0.5)
cpf = str(input('Digite seu CPF: '))
sleep(0.5)
endereço = str(input('Digite o seu endereço: '))
opcaoUsuario()


# Insetindo dados no banco
def insert(values, table, fields=None): # Valores, tabelas e campos 

    global c, con # Cursor e coneção

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

values = [f"DEFAULT, '{nome}', '{email}', '{senha}', '{sexo}', '{idade}', '{cpf}', '{endereço}'"]
insert(values, "pessoas")

print('Cadastrado com sucesso')