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

# Criar a inserção de dados
def inserir(conexao, sql, dados):
    try:
        c = conexao.cursor()
        c.execute(sql, dados)
        conexao.commit()
        print("Registro inserido!")
    except Error as ex:
        print(ex)

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vcon = ConexaoBanco()

vsql = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES(?,?,?)
    """
dados = (nome, telefone, email)

inserir(vcon, vsql, dados)
