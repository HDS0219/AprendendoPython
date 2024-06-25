#Criando função Tabuada
def tabuada():
    numero = 0
    #verificando se o número está entre 1 a 10.
    while numero < 1 or numero > 10:
        #Tratamento de exceção para caso o usuário não digite um número entre 1 e 10 ou digite algo fora do número inteiro.
        try:
            numero = int(input("Digite um número entre 1 a 10 para a tabuada: "))
            if numero < 1 or numero > 10:
                print("Entrada inválida.\n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro\n")

    #Mostrando na tela o resultado do número escolhido para a tabuada.
    print(f"Tabuada do número: {numero}")
    for i in range(1, 10):
        i += 1
        print(f"{numero} X {i} = {numero * i}")

#Looping while para verificar se o usúario ainda gostaria de ver outros números da tabuada, Se não, Finalizar o programa.
while True:
    tabuada()
    confirmacao = input("Deseja inserir outro número? (S/N): ")
    if confirmacao.upper() == "S":
        continue
    else:
        print("Fim do programa.")
        break
