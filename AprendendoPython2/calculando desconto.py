preco = float(input("Digite o preço do produto: R$"))
novo = preco - (preco * 5 / 100)

#forma 1
print(f"o produto com 5% de desconto custa {novo:.2f}R$")

print("="*12)

#forma 2
novo2 = float(input("digite as % para o desconto: "))
preco2 = preco - (preco * novo / 100)
print(f"o produto com {novo2} de deconto custa {preco2:.2f}R$")
