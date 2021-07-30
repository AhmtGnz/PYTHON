import time
t1 = time.time()


asal = [2,3,5,7]

a = 11

while a <= 100:
    
    for i in asal:
        bolundu = False
        if a%i == 0:
            bolundu = True
            break
        else:
            continue
    if bolundu == False:
        asal.append(a)
        
    
    a += 2

print(asal)


t2 = time.time()

print("Program süresi: ",t2-t1)