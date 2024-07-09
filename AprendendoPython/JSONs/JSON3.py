import json

'''

jogador = {
    "nome": "Bruno",
    "time": "aviadores",
    "vivo": "True",
    "energia": 100,
    "mochila": ["pederneira", "corda", "linha", "arame"],
    "aeronaves": [
        {"tipo": "transporte", "habilidade": 80},
        {"tipo": "ataque", "habilidade": 100},
        {"tipo": "reconhecimento", "habilidade": 50}
    ]
}
'''

jogador_j = '{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100},{"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)


#chaves
for c in jogador:
    print(c)

print("="*30)
#itens
for i in jogador.items():
    print(i)

print("="*30)
#valores
for v in jogador.values():
    print(v)

print("="*30)
#nome do jogador
print(jogador["nome"])

print("="*30)
#time
print(jogador["time"])

print("="*30)
#itens da mochila

for im in jogador["mochila"]:
    print(im)

print("="*30)
#aeronaves
for a in jogador["aeronaves"]:
    print(a)

print("="*30)
#tipos de aeronaves
for a in jogador["aeronaves"]:
    print(f"{a["tipo"]} - {a["habilidade"]}")