"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even (çiftse))
n → 3n + 1 (n is odd (tekse))

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""



import time

t1 = time.time()
degerler = [1]
lenler = [1]
for deger in range(1,1000001):
    print(deger)
    degerler.append(deger)
    say = 1
    
    liste = []
    liste.append(deger)
    while deger!=1:
        uzunluk = len(liste)
        if deger % 2 == 0:
            deger /= 2
            say += 1
        else:
            deger = 3*deger + 1
            say += 1
        liste.append(int(deger))
    lenler.append(len(liste))
    
a = lenler.index(max(lenler))

print("cevap: ",degerler[a])

t2 = time.time()
print("Geçen Zaman: {} saniye".format(round(t2-t1,3)))

"""
5 -6 dk da cevap bulundu.
"""