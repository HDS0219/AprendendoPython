import sqlite3
from sqlite3 import Error

# Função para criar conexão com o banco de dados SQLite3
def ConexaoBanco():
    caminho = "/agenda.db"  # Caminho para o banco de dados
    con = None
    try:
        con = sqlite3.connect(caminho)  # Tenta conectar ao banco de dados
    except Error as ex:
        print(ex)  # Imprime erro caso a conexão falhe
    return con

# Função para deletar dados na tabela
def deletar(conexao, sql):
    try:
        c = conexao.cursor()  # Cria um cursor para executar comandos SQL
        c.execute(sql)  # Executa o comando de deleção
        conexao.commit()  # Confirma as mudanças no banco de dados
    except Error as ex:
        print(ex)  # Imprime erro caso a deleção falhe
    finally:
        print("Registro removido")  # Mensagem de finalização

vcon = ConexaoBanco()  # Estabelece a conexão com o banco de dados

# Comando SQL para deletar um registro da tabela tb_contatos
vsql = """DELETE FROM tb_contatos WHERE N_IDCONTATO = 4
    """

deletar(vcon, vsql)  # Chama a função de deleção
