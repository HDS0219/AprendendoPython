num = int(input("digite um número para ver sua tabuada: "))

#forma 1
print(f"{num} X 1 = {num * 1}")
print(f"{num} X 2 = {num * 2}")
print(f"{num} X 3 = {num * 3}")
print(f"{num} X 4 = {num * 4}")
print(f"{num} X 5 = {num * 5}")
print(f"{num} X 6 = {num * 6}")
print(f"{num} X 7 = {num * 7}")
print(f"{num} X 8 = {num * 8}")
print(f"{num} X 9 = {num * 9}")
print(f"{num} X 10 = {num * 10}")


print("==========")
#forma 2

for i in range(1,11):
    print(f"{num} X {i} = {num * i}")