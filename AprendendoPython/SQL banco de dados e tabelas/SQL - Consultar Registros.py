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

# Função para consultar dados na tabela
def consulta(conexao, sql):
    c = conexao.cursor()  # Cria um cursor para executar comandos SQL
    c.execute(sql)  # Executa o comando de consulta
    resultado = c.fetchall()  # Obtém todos os resultados da consulta
    return resultado

vcon = ConexaoBanco()  # Estabelece a conexão com o banco de dados

# Comando SQL para selecionar todos os dados da tabela tb_contatos onde N_IDCONTATO é igual a 1
vsql = """SELECT * FROM tb_contatos WHERE N_IDCONTATO = 1"""

res = consulta(vcon, vsql)  # Chama a função de consulta e armazena os resultados

# Itera sobre os resultados e imprime cada registro
for r in res:
    print(r)

vcon.close()  # Fecha a conexão com o banco de dados
