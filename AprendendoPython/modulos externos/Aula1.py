import Aula2 as aula  # importando o modulo para esse arquivo

# Aula2 as aula muda o nome para não precisar chamar ela de "Aula2"

aula.canal_nome()
print(aula.jogador["nome"])

from Aula2 import jogador  # importa um modulo especifico

print(jogador["nome"])

import Aula2

res = dir(Aula2)

print(res)
