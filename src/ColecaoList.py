carros = ["HRV", "Golf", "Argo", "Focus"]
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

print(str(len(carros)) + " carros na lista")

print(carros)
carros = ["HRV", "Golf", "Argo", "Focus"]
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

print(str(len(carros)) + " carros na lista")

print(f"Carro 1: {carros[1]}") #format para teste mostrando o carro no indice 1("Golf")

carros.append("Fit") #adicionando carros
carros.append("Fusion")
carros.append("Polo")

carros.remove("Fusion") #removendo carro

print(str(len(carros)) + " carros na lista")

print(carros)
carros.pop() #remover o ultimo item da lista

del carros[2] #remover um item especifico
carros.clear() #Limpa todos os elementos da lista
carros2 = list(carros) #Copiar os itens de uma lista
carros2 = ["Fusca", "147", "Brasilia", "Celta"] #segunda lista criada para unir com a primeira

carros3 = carros + carros2 #unificar duas listas
carros = ["HRV", "Golf", "Argo", "Focus"] #List
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

carros2 = ["Fusca", "147", "Brasilia", "Celta"]

carros3 = carros + carros2

print(str(len(carros3)) + " carros na lista")

print(carros3)
#lista "indexavel"