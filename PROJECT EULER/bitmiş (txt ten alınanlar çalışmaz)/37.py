"""
Truncatable primes

The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

yukarıdaki örnek gibi soldan sağa ve sağdan sola tek tek basamak atarak da asal olan asal sayıların toplamını bul.
"""

import time

t1 = time.time()

def asal_mi(sayi):
    if sayi < 2:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2,sayi):
            if sayi%i == 0:
                return False
        return True

say = 0
sayi = 11
cevap = 0
while say != 11:
    sayi_str = str(sayi)
    ters = sayi_str[::-1]
    if not asal_mi(int(sayi_str[0])) or not asal_mi(int(sayi_str[0:2])) or not asal_mi(int(ters[0])):
        sayi += 2
        continue
    if asal_mi(sayi):
        say2 = 0
        # alttaki döngü süreyi uzatıyor sanki..
        for i in range(0,len(sayi_str)):
            if asal_mi(int(sayi_str[:i+1])) and asal_mi(int(sayi_str[i:len(sayi_str)])):
                say2 += 1
            else:
                break
        if say2 == len(sayi_str):
            say += 1
            cevap += sayi
            print(say, sayi, cevap)

    if sayi%10000 == 3:
        print(sayi)
    sayi += 2
print(cevap)

t2 = time.time()
print(t2-t1)

# cevap: 748317       (ilk 10 sayı hemen bulunuyor mesele son sayıda: 739397 )
# süre: 1438,6 sn : 2 dk 28 sn  