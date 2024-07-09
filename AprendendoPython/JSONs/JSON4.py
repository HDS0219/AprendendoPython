import json

tam = 50

#abrir o json externamente
#colocar no diretorio correto(removido por questões de privacidade)
with open("put the directory here") as f:
    jogador = json.load(f)

#chaves
for c in jogador:
    print(c)

print("="*tam)
#itens
for i in jogador.items():
    print(i)

print("="*tam)
#valores
for v in jogador.values():
    print(v)

print("="*tam)
#nome do jogador
print(jogador["nome"])

print("="*tam)
#time
print(jogador["time"])

print("="*tam)
#itens da mochila

for im in jogador["mochila"]:
    print(im)

print("="*tam)
#aeronaves
for a in jogador["aeronaves"]:
    print(a)

print("="*tam)
#tipos de aeronaves
for a in jogador["aeronaves"]:
    print(f"{a["tipo"]} - {a["habilidade"]}")