# importando SQLite3
import sqlite3

#criando conexão
try:
    con = sqlite3.connect('armazenamento.db')
    print("conexão com banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conecatar com banco de dados!", e)
##################################################################
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                ID INTEREGER PRiMARY KEY AUTOINCREMENT,
                MATRICULA TEXT,
                RAZAO_SOCIAL TEXT,
                NOME_FANTASIA TEXT,
                ENDERECO TEXT,
                BAIRRO TEXT,
                ATENDENTE TEXT
            )""")
        print("Tabela de clientes criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela de clientes", e)