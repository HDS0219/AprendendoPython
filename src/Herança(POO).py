class NPC:  # Classe pai / SuperClasse
    def __init__(self, nome, time, forca, municao): #construtor
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self): #função para exibir informações
        print(f"Nome: {self.nome}\nTime: {self.time}\nForça: {self.forca}\nMunição: {self.municao}\n"
              f"Vivo: {"Sim" if self.vivo else "Não"}\nenergia: {self.energia}")
        print("===========================================")

#classes filhos utilizam dentro do parentese a classe pai para herdar suas caracteristias
class Soldado(NPC): #Classe filho
    def __init__(self, nome, time): #construtor da classe filho pegando informações da classe pai e tranferindo a si mesmo informações que o difere da superclasse
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC): #classe filho
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC): #classe filho
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)

    def inf(self): #herdando uma função da função pai
        super().info()

#Exibindo informações das classes
s1 = Guarda("Player1", 1)
s2 = Soldado("Player2", 2)
s3 = Elite("Minecraft", 1)
s4 = Soldado("Boblox", 2)
s5 = Guarda("Terraria", 1)
s6 = Elite("X-tudo", 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf() #pegando informações atraves da herança "info"