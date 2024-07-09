import re  # Importa o módulo de expressões regulares(RegEx)

# Define o texto onde será realizada a pesquisa
texto = "Curso de Python. Caractere grande com frases aleatorias. Banana é uma fruta"

# Solicita ao usuário a entrada do termo de pesquisa
pesq = input("Pesquisar: ")

# Realiza a pesquisa usando findall, que retorna todas as correspondências na string
res = re.findall(pesq, texto)

# Imprime a lista de resultados encontrados
print(res)

# Conta o número de correspondências encontradas
qtde = len(res)

# Imprime a quantidade de correspondências
print(f"Quantidade: {qtde}")

# Itera sobre a lista de resultados e imprime cada correspondência encontrada
for t in res:
    print(t)
