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

vcon = ConexaoBanco()  # Estabelece a conexão com o banco de dados

# Comando SQL para criar a tabela tb_contatos
vsql = """ CREATE TABLE tb_contatos(
                N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOMECONTATO VARCHAR(30),
                T_TELEFONECONTATO VARCHAR(14),
                T_EMAILCONTATO VARCHAR(30)
        );"""

# Função para criar a tabela no banco de dados
def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()  # Cria um cursor para executar comandos SQL
        c.execute(sql)  # Executa o comando de criação de tabela
        print("Tabela criada!")  # Mensagem de sucesso
    except Error as ex:
        print(ex)  # Imprime erro caso a criação falhe

# Descomente a linha abaixo para criar a tabela
# criarTabela(vcon, vsql)

vcon.close()  # Fecha a conexão com o banco de dados
