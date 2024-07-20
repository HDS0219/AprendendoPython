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

# Função para inserir dados na tabela
def inserir(conexao, sql, dados):
    try:
        c = conexao.cursor()  # Cria um cursor para executar comandos SQL
        c.execute(sql, dados)  # Executa o comando de inserção com os dados fornecidos
        conexao.commit()  # Confirma as mudanças no banco de dados
        print("Registro inserido!")  # Mensagem de sucesso
    except Error as ex:
        print(ex)  # Imprime erro caso a inserção falhe

# Entrada de dados do usuário para inserção
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vcon = ConexaoBanco()  # Estabelece a conexão com o banco de dados

# Comando SQL para inserir dados na tabela tb_contatos
vsql = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES(?,?,?)
    """
dados = (nome, telefone, email)  # Dados a serem inseridos

inserir(vcon, vsql, dados)  # Chama a função de inserção
