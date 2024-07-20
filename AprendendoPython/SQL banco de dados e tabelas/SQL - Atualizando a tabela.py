import sqlite3
from sqlite3 import Error


# Criar conexão com SQLite3
def ConexaoBanco():
    caminho = "/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


# Criar a atualização de dados
def atualizar(conexao, sql, dados):
    try:
        c = conexao.cursor()
        c.execute(sql, dados)
        conexao.commit()
        print("Registro atualizado!")
    except Error as ex:
        print(ex)


idcontato = int(input("Digite o id a ser atualizado: "))
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vcon = ConexaoBanco()

vsql = """UPDATE tb_contatos 
            SET T_NOMECONTATO = ?, T_TELEFONECONTATO = ?, T_EMAILCONTATO = ?
            WHERE N_IDCONTATO = ?
    """
dados = (nome, telefone, email, idcontato)

atualizar(vcon, vsql, dados)

vcon.close()
