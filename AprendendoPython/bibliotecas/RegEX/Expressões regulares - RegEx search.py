import re  # Importa o módulo de expressões regulares

# Define o texto onde será realizada a pesquisa
texto = "Curso de Python. Caractere grande com frases aleatórias. Banana é uma fruta"

# Realiza a pesquisa pela palavra "Python" no texto
res = re.search("Python", texto)

# Verifica se a pesquisa encontrou algum resultado
if res is not None:
    # Imprime a posição inicial da correspondência encontrada
    print(res.start())

    # Imprime a posição final da correspondência encontrada
    print(res.end())

    # Calcula o tamanho da string correspondente
    pi = res.start()  # Posição inicial
    pf = res.end()    # Posição final
    tam = pf - pi     # Tamanho da string correspondente

    # Imprime o tamanho da string correspondente
    print(tam)
else:
    # Informa que a palavra não foi encontrada no texto
    print("não encontrado!")
