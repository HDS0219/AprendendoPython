def somar(): #exemplo fácil para uma fácil compreensão
    print("Somei")
    print("Somado\n")

somar()
somar()
somar()

#função para somar e subtrair

n1 = 15
n2 = 7

def somar():
    r = n1 + n2
    print(f"Soma de {n1} e {n2} = {r}")

def subtrair():
    r = n1 - n2
    print(f"Subtração de {n1} e {n2} = {r}")

somar() #chamar função soma
subtrair()

#função para todos os tipos de calculos

n1 = 15
n2 = 7

def somar():
    r = n1 + n2
    print(f"Soma de {n1} e {n2} = {r}")

def subtrair():
    r = n1 - n2
    print(f"Subtração de {n1} e {n2} = {r}")

def multiplicacao():
    r = n1 * n2
    print(f"multriplicação de {n1} e {n2} = {r}")

def divisao():
    r = n1 / n2
    print(f"divisão de {n1} e {n2} = {r}")

def calculos(): #chamar funções dentro de função
    somar()
    subtrair()
    multiplicacao()
    divisao()

calculos() #chamar a função que chama as funções

#utilizando parametros de entrada
def somar(n1,n2): #parametros de entrada
    r = n1 + n2
    print(f"Soma de {n1} e {n2} = {r}")

somar(5,7)
somar(12,8)
somar(1,2)

#outro exemplo:
def somar(n1, n2, n3, n4): #parametros de entrada
    r = n1 + n2 + n3 + n4
    print(f"Soma dos valores é {r}")

somar(5,7,3,2)
somar(12,8,1,20)
somar(1,2,0,0)

#codigo arbitrario
def textos(txt):  # argumento arbitrario: | passando qualquer numero de argumentos
    for t in txt:
        print(t)


textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")
#outro exemplo:

def somar(num):  # parametros de entrada
    r = 0
    for n in num:
        r += n
    print(f"Soma dos valores é {r}")


def textos(txt):  # argumento arbitrario: * | passando qualquer numero de argumentos
    for t in txt:
        print(t)

somar(1,2,3,4)
#textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")def somar(num):  # parametros de entrada
    r = 0
    for n in num:
        r += n
    print(f"Soma dos valores é {r}")


def textos(txt):  # argumento arbitrario: * | passando qualquer numero de argumentos
    for t in txt:
        print(t)

somar(5,2)
#textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

#mais exemplos de parametros
def carros(c):
    print(f"Modelo: {c}")

carros("HRV")

#parametro com valor padrão
def carros(c = "Golf"): #se eu não por parametro então ele vai no valor padrão
    print(f"Modelo: {c}")

carros()

#parametros de entrada com lista

valores = [1, 5, 3, 2]
def somar(num):  # parametros de entrada
    r = 0
    for n in num:
        r += n
    print(f"Soma dos valores é {r}")

somar(valores)

#usando return
valores = [1, 5, 3, 2]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r #retorno do valor

print(somar(valores))

#mais exemplos
valores = [1, 5, 3, 2]

def somar(num):
    r = 0
    for n in num:
        r += n
    return r

def valLista(num):
    for v in num:
        print(v)

print(f"{valores}: soma = {somar(valores)}")

#ultimo exemplo
valores = [1, 5, 3, 2]

def somar(num):
    r = 0
    for n in num:
        r += n
    return r

r = somar(valores)#forma alternativa

print(f"{valores}: soma = {r}")
