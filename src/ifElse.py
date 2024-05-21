clima = "sol"
dinheiro = 500
lugar = ""

if clima == "sol" and dinheiro > 300:
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao " + lugar)
condição if e else
clima = "sol"
dinheiro = 5000
lugar = ""

if clima == "sol" and (dinheiro > 300 and dinheiro < 500): #dinheiro entre 300 e 500
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao " + lugar)
if clima == "sol" or (dinheiro > 300 and dinheiro < 500): #uma condição verdadeiro para ser verdadeiro
    lugar = "clube"
else:
    lugar = "cinema"