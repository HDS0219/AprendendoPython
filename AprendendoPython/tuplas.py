t_carros = ("HRV", "Golf", "Argo")
l_carros = list(t_carros)
l_carros[2] = "Focus"
t_carros = tuple(l_carros)

#t_carros[2] = "Focus"
#print(t_carros[0])

for x in t_carros:
    print(x)