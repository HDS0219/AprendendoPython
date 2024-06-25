import json  # importando o módulo JSON

# String JSON (semelhante a um dicionário em Python)
carros_json = ('{'
               '"marca":"honda",'
               '"modelo":"HRV",'
               '"cor":"prata"'
               '}')

# json.loads carrega a string JSON e a transforma em um dicionário
carros = json.loads(carros_json)

# Acessa e imprime o valor associado à chave "modelo"
#print(carros["modelo"])

#faz o looping mostrando os valores do JSON
for i in carros.values():
    print(i)

print("=========")

#faz o looping mostrando os itens com key e value
for k,v in carros.items():
    print(f"{k} = {v}")

print("=========")

#Transformar dicionário em JSON
carros2 = ('{'
               '"marca":"honda",'
               '"modelo":"HRV",'
               '"cor":"prata"'
               '}')

# Converte o dicionário em uma string JSON
carros2_json = json.dumps(carros2)