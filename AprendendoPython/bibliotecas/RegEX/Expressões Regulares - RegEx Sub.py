import re

# Texto original
texto = "Curso de Python. Caractere grande com frases aleatórias. Banana é uma fruta"

# Substituir espaços por hífens
res = re.sub("\s", "-", texto)

# Substituir vírgulas por pontos
res = re.sub(",", ".", res)

print(res)
