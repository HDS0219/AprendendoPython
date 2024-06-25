def analisando_palavras(): #Criada a função para analisar palavras.
    vogais = "aeiouAEIOUáéíóúàèìòùâêîôûÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛãõÃÕ"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    numero_vogais = 0
    numero_consoantes = 0

    #looping para verificar se a palavra selecionada contém apenas caracteres apresentados acima
    while True:
        palavras = input("Insira uma palavra a ser analisada: ")

        #se não passar do teste, repete o input anterior
        if not palavras.isalpha():
            print("Digite apenas uma palavra, não números, caractere especial ou mais de uma palavra.")
            continue

        #looping para calcular as letras das palavras
        for letra in palavras:
            if letra in vogais:
                numero_vogais += 1
            elif letra in consoantes:
                numero_consoantes += 1

        #mostrando na tela se as palavras começam com maiúscula ou minúscula
        if palavras[0].isupper():
            print("A palavra começa a com a letra maiúscula")
        elif palavras[0].islower():
            print("A palavra começa com a letra minúscula")

        #mostrando todos os resultados na tela de números de palavras, vogais e consoantes
        print(f"A palavra contem {len(palavras)} letras")
        print(f"A palavra contem {numero_vogais} vogais")
        print(f"A palavra contem {numero_consoantes} consoantes")

        #saindo do looping caso termine de analisar
        break

#Looping para verificar se o usuario gostaria de tentar uma outra palavra a ser analisada
while True:
    analisando_palavras()
    confirmacao = input("Deseja inserir outra palavra? (S/N): ")
    if confirmacao.upper() == "S":
        continue
    else:
        print("Fim do programa.")
        break
