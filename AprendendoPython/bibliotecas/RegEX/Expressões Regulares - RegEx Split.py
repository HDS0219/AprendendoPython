import re  # Importa o módulo de expressões regulares

# Define o texto a ser dividido
texto = "Curso de Python. Caractere grande com frases aleatórias. Banana é uma fruta"

# Divide o texto nos espaços em branco usando re.split
res = re.split("\s", texto)

# Imprime a lista de palavras resultantes da divisão
print(res)

# Imprime o terceiro elemento da lista (índice 2)
print(res[2])

# Itera sobre a lista de palavras e imprime cada uma
for t in res:
    print(t)
