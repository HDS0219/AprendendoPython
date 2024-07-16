import re
import os

# Definindo o nome do arquivo e o caminho onde ele está localizado
nome = "teste2.txt"
caminho = "escolha o caminho"

# Verificando se o arquivo existe no caminho especificado
if os.path.exists(caminho + nome):
    print("Arquivo existente")
else:
    # Se o arquivo não existir, cria um novo arquivo
    print("Arquivo inexistente\nCriando arquivo...")
    with open(caminho + nome, "x") as f:
        pass  # Cria o arquivo e fecha imediatamente

# Abrindo o arquivo no modo de leitura de texto ('rt')
with open(caminho + nome, "rt") as f:
    pass  # Fecha o arquivo após abrir para leitura

# Removendo o arquivo
os.remove(caminho + nome)
