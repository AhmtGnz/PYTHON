def okek(x,y):
    if x<y:
        küçük,büyük = x,y
    else:
        küçük,büyük = y,x
    
    for i in range(1,küçük+1):
        if (büyük*i) % küçük == 0:
            return büyük*i
            
        
x = int(input("x:"))
y = int(input("y:"))

print(okek(x,y))