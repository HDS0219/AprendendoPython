metros = float(input("Distância em metros: "))

#forma 1(tive preguiça de fazer com quebra de linha)
print(f"A medida de {metros} corresponde a: ")
print(f"{metros / 1000} KM")
print(f"{metros / 100} HM")
print(f"{metros / 10} DAM")
print(f"{metros * 10} DM")
print(f"{metros * 100} CM")
print(f"{metros * 1000} MM")

print("===============")

#forma 2
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f"A medida de {metros} corresponde a: \n{km} KM \n{hm} HM \n{dam} DAM \n{dm} DM \n{cm} CM \n{mm} MM")