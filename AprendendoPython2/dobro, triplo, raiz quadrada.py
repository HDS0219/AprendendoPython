from math import sqrt

num = int(input("Digite um número: "))
print(f"O dobro de {num} vale {num * 2}\n O triplo de {num} vale {num * 3}\n A raiz quadrada de {num} é {sqrt(num):.2f}") # forma 1

print("==========================")

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f"O dobro de {num} vale {dobro}\n O triplo de {num} vale {triplo}\n A raiz quadrada de {num} é {raiz:.2f}") # forma 2

print("==========================")

print(f"O dobro de {num} vale {dobro}\n O triplo de {num} vale {triplo}\n A raiz quadrada de {num} é {pow(num, (1/2))}") # forma 3