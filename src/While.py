carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]
i = 0
tam = len(carros)
while i < tam:
    print(carros[i])
    i+=1
print("\nfim do loop")
carros = []
carro = input("Digite o nome do novo carro: ")
tam = len(carros)
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

for x in carros:
    print(x)

print("\nfim do loop")