print("""
**************
ÇARPIM TABLOSU
**************
""")

liste = [*range(1,10)]

for i in liste:
    print("\n************\n")
    for j in liste:
        print("{} x {} = {}".format(i,j,i*j))
        