# Donato-Bank
- A simple registration project combining the Python language and the Mysql database

![python-mysql-logo](https://user-images.githubusercontent.com/51414398/81754862-93d91b00-948d-11ea-951d-020dac250574.jpg)

## Why ?
- Just for practice and fun :D

## Let's go to the code

### Modules
Importing Libraries

<details><summary>MySql</summary>
  Importing the MySQL library
</details>

```
import MySQLdb
```

<details><summary>Sleep</summary>
  Importing the sleep library
</details>

```
from time import sleep
```

### Bank details

<details><summary>Data</summary>
  Your bank details to connect
</details>

```
host = "o host"
user = "seu usuario"
password = "sua senha"
db = "nome do banco"
port = "porta" # Example: 3306
```

<details><summary>Connecting with bank</summary>
  Connecting to your bank variables
</details>

```
con = MySQLdb.connect(host, user, password, db, port)
```

<details><summary>Taking the result</summary>
  Result
</details>

```
c = con.cursor() 
```
### Menu
Interactivity menu

<details><summary>Menu</summary>
  Welcome
</details>

```
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
```

### Register


<details><summary>User Register/summary>
  Where user will register
</details>

```
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
```

### Inserting Data

<details><summary>Conecting and Inserting</summary>  
inserting data into the bank
</details>

```
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
```

