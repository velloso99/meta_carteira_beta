# importando SQLite3
import sqlite3

#criando conexão
try:
    con = sqlite3.connect('armazenamento.db')
    print("conexão com banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conecatar com banco de dados!", e)
########################################################################
#Criando tabela cadastro de clientes
def cadastrar_clientes(i):
    with con:
        cur - con.cursor()
        query = "INSERT INTO clintes()"
        cur.execute(query, i)






