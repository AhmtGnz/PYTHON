print("""
*******************
FAKTÖRİYEL BULMA
*******************
""")

değer = int(input("x:"))

liste = [*range(1,değer+1)]

f = 1

for i in liste:
    f *= i
    
print("{}'in faktöriyeli= {}".format(değer,f))
    
print(2*2*2*3*5*3*7)