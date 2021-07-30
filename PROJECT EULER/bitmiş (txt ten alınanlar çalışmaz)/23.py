"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 

the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


mükemmel sayı : kendisi hariç bölenlerinin toplamı kendisine eşit olan sayı
                    örnek: 28 (1+2+4+7+14 = 28)
dar sayı: toplam < sayı
geniş sayı: toplam > sayı
    en küçük geniş sayı: 12 (1+2+3+4+6 = 16)

en küçük iki geniş sayının toplamı = 24 (12+12)
28123 den büyük olan sayılar iki geniş sayının toplamı olarak yazılabiliyor

iki geniş sayının toplamı şeklinde yazılamayan tüm sayıların toplamını bul.

"""

import time

t1 = time.time()

def genis_sayi(x):
    toplam = 1
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            toplam += i
    
            if toplam > x:
                return True            
            else:
                continue        
        else:
            continue
    return False


genis_sayilar = []
for i in range(12,28123):
    if genis_sayi(i):
        genis_sayilar.append(i)


n = 28123
genel_toplam = (n * (n+1)) / 2
kume = set()

for i in genis_sayilar:
    for j in genis_sayilar:
        if i+j <= 28123 and i <= j:
            kume.add(i+j)


print(int(genel_toplam - sum(list(kume))))

t2 = time.time()

print(t2 - t1)


# cevap : 4179871 
# 22 sn
