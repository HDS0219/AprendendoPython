a = 10
b = 5
res = 0
op = "x"

if op == "+":
    res = a+b
if op == "-":
    res = a-b
if op == "/":
    res = a/b
if op == "x":
    res = a*b

print(str(a) + op + str(b) + " = " + str(res))
#=========================================================#
a = 10
b = 5
res = 0
op = "-"

if op == "+":
    res = a+b
elif op == "-":
    res = a-b
elif op == "/":
    res = a/b
elif op == "x":
    res = a*b
else:
    print("NULL")

print(str(a) + op + str(b) + " = " + str(res)) #melhoria que eu coloquei