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




