carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion","Golf","Focus","Onyx","Fit"] #criando a lista com uma grande quantia
itCarros = iter(carros)

while itCarros: #looping while não precisa especificar aonde vai parar, pois o proprio progama ira parar quando chegar ao final da lista e tentar passar
    try:
        print(next(itCarros)) #percorrer toda a lista
    except StopIteration:
        print("Fim da lista")
        break #parar o looping do "fim da lista"
#Iterator é uma função que ajuda em criação de lista para não precisar controlar o tamanho dela caso queira percorrer ela inteira