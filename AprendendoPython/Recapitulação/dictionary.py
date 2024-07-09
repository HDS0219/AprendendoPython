#Chave/key - Valor/Value
carro = {
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}

carro["Cambio"] = "Automatico"
del carro["Cambio"]

#carro.pop("Cambio") #remover o cambio

fab = carro["Fabricante"]
#fab = carro.get("Fabricante")

carro["Cor"] = "Preto"

carro.clear() #limpa todas as chaves e itens

print("Tamanho do Dictionary: " + str(len(carro)) + "\n")

if "Modelo" in carro:
    print("SIM, modelo é uma chave\n")

for c, v in carro.items():
    print(c + ": " + v)

#=============================================================#
Carro1 = {
    "Fabricante": "Honda",
    "Modelo": "HRV"
}
Carro2 = {
    "Fabricante": "Volkswagem",
    "Modelo": "Golf"
}
Carro3 = {
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

Carros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}

print(Carros["C1"]["Modelo"])
#diversas chaves