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
        cur=con.cursor()
        query = "INSERT INTO clientes(matricula,razao_social,nome_fantasia,endereco,bairro,atendente) values(?,?,?,?,?,?)"
        cur.execute(query, i)
####################################################################
#Ver Clientes
def ver_clientes():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM clientes')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista 
# Atualizar clients(update U)--------------------------------------------------
def atualizar_clientes(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET name=?, cpf=?,genero=?, email=?, telefone=?, endereco=?,cep=?, bairro=?, municipio=?, tutor=?, data_nascimento=?, ano_letivo=?, foto=? WHERE id=?"
        cur.execute(query, i)
# Deletar clientes(deletar D)----------------------------------------------------
def deletar_clientes(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM clientes WHERE id=?"
        cur.execute(query, i)



