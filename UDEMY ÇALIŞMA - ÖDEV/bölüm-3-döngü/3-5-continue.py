print("\n\nContinue yi Kullanma Deneyimi\n")

liste = [*range(1,101)]
liste2 = []

for i in liste:
    if i % 3 != 0:
        continue
    else:
        liste2.append(i)
print(liste2,"\n")