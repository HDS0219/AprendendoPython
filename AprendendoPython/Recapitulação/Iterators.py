# Cria uma lista de carros
carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Focus", "Onyx", "Fit"]

# Cria um iterador para a lista de carros
itCarros = iter(carros)

# Loop while para percorrer todos os elementos do iterador
while itCarros:
    try:
        # Imprime o próximo elemento do iterador
        print(next(itCarros))
    except StopIteration:
        # Quando o iterador é esgotado, uma exceção StopIteration é lançada
        print("Fim da lista")
        break  # Sai do loop quando o fim da lista é alcançado

# Observação: Iteradores são úteis para percorrer listas sem precisar gerenciar manualmente o tamanho da lista
