import random
import os

erros = 0
sorteado = random.randrange(0,100)
jogador = int(input("Digite seu número entre 1 a 100: "))

while(sorteado != jogador):
    os.system('cls')
    if(sorteado > jogador):
        print("Erro, o número é maior.")
    elif(sorteado < jogador):
        print("Erro, o número é menor.")
    erros+=1
    jogador = int(input("Digite seu número entre 1 a 100: "))

print(f"Número {jogador}, você acertou em {erros+1}")
#futuramente criar uma versão para remover o system32