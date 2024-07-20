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

# Função para atualizar dados na tabela
def atualizar(conexao, sql, dados):
    try:
        c = conexao.cursor()  # Cria um cursor para executar comandos SQL
        c.execute(sql, dados)  # Executa o comando de atualização com os dados fornecidos
        conexao.commit()  # Confirma as mudanças no banco de dados
        print("Registro atualizado!")  # Mensagem de sucesso
    except Error as ex:
        print(ex)  # Imprime erro caso a atualização falhe

# Entrada de dados do usuário para atualização
idcontato = int(input("Digite o id a ser atualizado: "))
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vcon = ConexaoBanco()  # Estabelece a conexão com o banco de dados

# Comando SQL para atualizar os dados na tabela tb_contatos
vsql = """UPDATE tb_contatos 
            SET T_NOMECONTATO = ?, T_TELEFONECONTATO = ?, T_EMAILCONTATO = ?
            WHERE N_IDCONTATO = ?
    """
dados = (nome, telefone, email, idcontato)  # Dados a serem atualizados

atualizar(vcon, vsql, dados)  # Chama a função de atualização

vcon.close()  # Fecha a conexão com o banco de dados
