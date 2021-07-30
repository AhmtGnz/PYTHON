def obeb(x,y):
    if x<y:
        küçük,büyük = x,y
    else:
        küçük,büyük = y,x
        
    for i in range(küçük,1,-1):
        if küçük % i == 0:
            if büyük % i ==0:
                çözüm = i
                return çözüm
    return "{} ve {} aralarında asal sayıdır.".format(x,y)
    
x = int(input("x:"))
y = int(input("y:"))

print(obeb(x,y))