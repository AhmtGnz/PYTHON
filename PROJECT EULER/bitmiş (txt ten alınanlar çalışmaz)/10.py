import time
t1 = time.time()


asal = [2,3,5,7]
toplam = 17
a = 11

while a <= 100000:  
    
    for i in asal[:len(asal)//3]:
        bolundu = False
        if a%i == 0:            
            bolundu = True
            break
        else:
            continue
    if bolundu == False:
        asal.append(a)
        toplam += a
    
    a += 2


print("toplam:",toplam)



t2 = time.time()

print("Program süresi: ",t2-t1)