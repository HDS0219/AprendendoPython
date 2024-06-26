soma = lambda a,b: a+b #expressão "lambda" ou expressão "anonima" não precisa por nome
print(soma(2,5))

#mais exemplos

soma = lambda a, b: a + b
mult = lambda a, b, c: (a + b) * c
print(soma(2, 5))
print(mult(2,5,3))

#exemplo3
(lambda a, b: a + b)(3,2) #também funciona pois não precisa armazenar ou associar com algo
print((lambda a, b: a + b)(3,2))
r = lambda x, func: x + func(x)
res = r(2, lambda x:x*x)
print(res)

#exemplo 4
r = lambda x, func: x + func(x)
res = r(3, lambda x:xx)
print(res) #x + função de "X" que é X vezes X então vai me retornar: X + X X

#exemplo 5r = lambda x, func: x + func(x)
res = r(2, lambda x: x * x) 2 + 2 * 2
print(res)
res = r(2, lambda x: x + x) # 2 + 2 + 2
print(res)

