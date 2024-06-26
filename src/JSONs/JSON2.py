import json

carros_dictionary = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
# dicionary -> array json

carros_list = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]
# list -> array json

carros_tupla = ("honda", "volkswagem", "ford", "fiat", "chevrolet")
# tupla -> array json
# json não reconhece a tupla, então trata a tupla como array/list

carros_j = json.dumps(carros_dictionary, indent=4, separators=(":", "="), sort_keys=True)
# usar o indent faz a formatação dando espaços
# separators substitui o caractere
# sort_keys ordena as chaves por ordem alfabetica

print(carros_j)
