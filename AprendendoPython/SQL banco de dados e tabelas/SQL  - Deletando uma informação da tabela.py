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

# Deletar dados
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")

vcon = ConexaoBanco()

vsql = """DELETE FROM tb_contatos WHERE N_IDCONTATO = 4
    """


deletar(vcon, vsql)
