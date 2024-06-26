import os

carros = []  # Lista de Carros criada


class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print(
            f"Nome: {self.nome}\n"
            f"Potência: {self.pot}\n"
            f"Velocidade maxima: {self.velMax}\n"
            f"ligado: {"sim" if self.ligado == True else "Não"}")


def Menu(): #menu para o sistema de carros
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair")
    print(f"Quantidade de carros:{len(carros)}")
    opc = input("Digite uma opção: ")
    return opc  # usuario vai digitar e vai retornar para a opção que ele selecionou


def NovoCarro():
    os.system("cls") or None
    n = input("Nome do Carro: ")
    p = input("Potência do Carro: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro")
    os.system("pause")


def informacoes():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")


def excluirCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja Excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro não existe na lista")
    os.system("pause")


def ligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja Ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")


def desligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja Ligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")


def listarCarros():
    os.system("cls") or None
    p = 0
    for c in carros:
        print(f"{p} - {c.nome}")
        p = p + 1

    os.system("pause")

ret = Menu()
while ret < "7":
    if ret == "1":
        NovoCarro()
    elif ret == "2":
        informacoes()
    elif ret == "3":
        excluirCarro()
    elif ret == "4":
        ligarCarro()
    elif ret == "5":
        desligarCarro()
    elif ret == "6":
        listarCarros()
    ret = Menu()

os.system("cls") or None
print("Programa finalizado")