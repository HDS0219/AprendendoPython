curso = "Curso de Python"



print(curso[9:15]) #string de caracteres
print(curso.strip()) #remove espaço no começo e final
print(curso.lower().strip()) #minusculo
print(curso.upper()) #maiusculo
print(curso.replace("Python","C#")) #troca de caracteres
a = print(curso.split(" "))
print(a[0]) #transformar palavras inteiras em list
print("Tamanho: " + str(len(curso)))

texto = "Curso de Python"
print(curso[9:15]) #string de caracteres
print(curso.strip()) #remove espaço no começo e final
print(curso.lower().strip()) #minusculo
print(curso.upper()) #maiusculo
print(curso.replace("Python","C#")) #troca de caracteres
a = print(curso.split(" "))
print(a[0]) #transformar palavras inteiras em list
print("Tamanho: " + str(len(curso)))

res = "python" in texto # "in" verifica se tem uma palavra em "texto". "not in" o mesmo so que negando
print(res)

curso = "Curso de Python"
canal = "CBF Cursos"

res = curso + " do canal " + canal

res = palavra.upper() in texto.upper()

print(res)
cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano = 2019


res = palavra.upper() in texto.upper()

print(f"cidade, {cidade}, dia {dia} de mes {mes} de {ano}")