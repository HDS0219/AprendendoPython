import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1 = CPU - 2 = Jogador
maxJogadas = 9
vit = 'n'
velha = [
    [" ", " ", " "],  # L0C0 L0C1 L0C2
    [" ", " ", " "],  # L1C0 L1C1 L1C2
    [" ", " ", " "]  # L2C0 L2L1 L2C2
]


def tela():
    global velha
    global jogadas
    os.system("cls") or None
    print("    0   1   2")
    for i in range(3):
        print(f"{i}:  {velha[i][0]} | {velha[i][1]} | {velha[i][2]}")
        if i < 2:
            print("   -----------")
    print(f"Jogadas: {Fore.GREEN} {jogadas}  {Fore.RESET}")


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna é inválido.")


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 2


def verificarvitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # Verificar vitoria em linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break
        # Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break
        # verifica diagonal 1
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if (velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2  # 1 = CPU - 2 = Jogador
    maxJogadas = 9
    vit = 'n'
    velha = [
        [" ", " ", " "],  # L0C0 L0C1 L0C2
        [" ", " ", " "],  # L1C0 L1C1 L1C2
        [" ", " ", " "]  # L2C0 L2L1 L2C2
    ]

while(jogarNovamente == "s"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarvitoria()
        if (vit != "n") or (jogadas >= maxJogadas):
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if (vit == "X" or vit == "O"):
        print(f"Resultado: Jogador {vit} venceu!")
    else:
        print("Resultado: velha")
    jogarNovamente = input(f"{Fore.BLUE}Jogar Novamente? [s/n]:{Fore.RESET}")
    redefinir()

