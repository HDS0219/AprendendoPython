import os
import sqlite3
from sqlite3 import Error

# Caminho do banco de dados
caminho = "/agenda.db"

# Função para conectar ao banco de dados
def ConexaoBanco():
    # Verifica se o arquivo do banco de dados existe
    if os.path.exists(caminho):
        con = None
        try:
            # Tenta estabelecer uma conexão com o banco de dados
            con = sqlite3.connect(caminho)
        except Error as ex:
            # Em caso de erro, exibe a mensagem de erro
            print(ex)
        # Retorna a conexão estabelecida
        return con
    else:
        # Caso o arquivo do banco de dados não exista, exibe uma mensagem de erro e encerra o programa
        print("Error! Caminho ou arquivo inexistente.")
        exit()

# Estabelece a conexão com o banco de dados
vcon = ConexaoBanco()

# Função para executar uma query no banco de dados
def query(conexao, sql, dados=None):
    try:
        c = conexao.cursor()
        # Verifica se há dados para serem inseridos na query
        if dados:
            c.execute(sql, dados)
        else:
            c.execute(sql)
        # Confirma as alterações no banco de dados
        conexao.commit()
    except Error as ex:
        # Em caso de erro, exibe a mensagem de erro
        print(ex)
    finally:
        # Exibe uma mensagem de sucesso após a operação
        print("Operação Realizada com sucesso")

# Função para consultar dados no banco de dados
def consultar(conexao, sql, dados=None):
    try:
        c = conexao.cursor()
        # Verifica se há dados para serem inseridos na query
        if dados:
            c.execute(sql, dados)
        else:
            c.execute(sql)
        # Retorna os resultados da consulta
        res = c.fetchall()
        return res
    except Error as ex:
        # Em caso de erro, exibe a mensagem de erro
        print(ex)
        return None

# Função para exibir o menu principal
def menuPrincipal():
    # Limpa a tela
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro por ID")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

# Função para inserir um novo registro no banco de dados
def menuInserir():
    os.system("cls" if os.name == "nt" else "clear")
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")

    # SQL para inserir um novo registro
    vsql = """ INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
               VALUES(?,?,?)
        """
    dados = (vnome, vtelefone, vemail)
    vcon = ConexaoBanco()
    query(vcon, vsql, dados)
    vcon.close()

# Função para deletar um registro do banco de dados
def menuDeletar():
    os.system("cls" if os.name == "nt" else "clear")
    vDeletarId = input("Digite o ID do registro a ser deletado: ")

    # SQL para deletar um registro pelo ID
    vsql = '''
    DELETE FROM tb_contatos WHERE N_IDCONTATO = ?
    '''
    dados = (vDeletarId,)
    query(vcon, vsql, dados)

# Função para atualizar um registro no banco de dados
def menuAtualizar():
    os.system("cls" if os.name == "nt" else "clear")
    vAtualizar = input("Digite o ID do registro a ser modificado: ")
    # Consulta o registro pelo ID
    r = consultar(vcon, "SELECT * FROM tb_contato WHERE N_IDCONTATO = ?", (vAtualizar,))

    if not r:
        print("Registro não encontrado.")
        return

    rNome = r[0][1]
    rTelefone = r[0][2]
    rEmail = r[0][3]

    # Solicita novos dados ou mantém os atuais
    vnome = input(f"Digite o nome ({rNome}): ") or rNome
    vtelefone = input(f"Digite o telefone ({rTelefone}): ") or rTelefone
    vemail = input(f"Digite o email ({rEmail}): ") or rEmail

    # SQL para atualizar o registro
    vsql = ("UPDATE tb_contatos "
            "SET T_NOMECONTATO = ?, T_TELEFONECONTATO = ?, T_EMAILCONTATO = ? "
            "WHERE N_IDCONTATO = ?")

    dados = (vnome, vtelefone, vemail, vAtualizar)

    query(vcon, vsql, dados)

# Função para consultar um registro pelo ID
def menuConsultarId():
    os.system("cls" if os.name == "nt" else "clear")
    vId = input("Digite o ID do registro a ser consultado: ")
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO = ?", (vId,))
    if r:
        for reg in r:
            print(f"ID: {reg[0]}")
            print(f"Nome: {reg[1]}")
            print(f"Telefone: {reg[2]}")
            print(f"Email: {reg[3]}")
    else:
        print("Registro não encontrado.")

# Função para consultar um registro pelo nome
def menuConsultarNome():
    os.system("cls" if os.name == "nt" else "clear")
    vNome = input("Digite o nome do registro a ser consultado: ")
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE ?", ('%' + vNome + '%',))
    if r:
        for reg in r:
            print(f"ID: {reg[0]}")
            print(f"Nome: {reg[1]}")
            print(f"Telefone: {reg[2]}")
            print(f"Email: {reg[3]}")
    else:
        print("Registro não encontrado.")

# Loop principal do programa
opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    # Opções do menu principal
    match opc:
        case 1:
            menuInserir()
        case 2:
            menuDeletar()
        case 3:
            menuAtualizar()
        case 4:
            menuConsultarId()
        case 5:
            menuConsultarNome()  # Corrige o nome da função
        case 6:
            os.system("cls" if os.name == "nt" else "clear")
            print("Programa finalizado")
        case _:
            os.system("cls" if os.name == "nt" else "clear")
            print("Opção inválida")
            os.system("pause")

os.system("pause")
