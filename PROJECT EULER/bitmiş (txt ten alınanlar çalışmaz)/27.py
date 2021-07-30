"""
Quadratic primes
    ikinci derece asallar

Euler discovered the remarkable quadratic formula:  

n**2 + n + 41
    bu formül ile 0 dan 39a kadar (0,39 dahil) tüm sayılar asal sayı veriyor.

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
However, when n = 40 is divisible by 41, and certainly when n = 41 is clearly divisible by 41.


The incredible formula;
n**2 - 79*n + 1601
    bu formülde 79a kadarki sayılardan asal sayı veriyor.

was discovered, which produces 80 primes for the ‎consecutive integer values‎ 0 <= n <= 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    ikinci dereceden formüller ele alınarak;  n**2 + a*n + b   (|a| <= 1000  ve |b| <= 1000)


Find the product of the coefficients, a and b,  
for the quadratic expression that produces the maximum number of primes for ‎consecutive values‎ of n, starting with 0.

a ve b için verilen aralıkta max n için a*b yi bul.

"""


import time

t1 = time.time()

def asal_mi(sayı):
    if (sayı == 1):
        return False

    elif (sayı == 2):
        return True

    else:
        for i in range(2,int(sayı/2)+1):
            if (sayı % i == 0):
                return False
        return True


def formul(a,b):
    n = 0
    while True:
        fn = n * (n + a) + b
        
        if fn > 0 and asal_mi(fn):
            n += 1

        else:
            return n-1
    return n-1

liste_a = [i for i in range(-1000,1001) if not i%2 == 0]
liste_b = [i for i in range(2,1000) if asal_mi(i)]

liste_n = []
liste_a2 = []
liste_b2 = []

for a in liste_a:
    print(a)
    for b in liste_b:
        liste_n.append(formul(a, b))
        liste_a2.append(a)
        liste_b2.append(b)
        

index = liste_n.index(max(liste_n))

print("max n:", liste_n[index], "\na,b: ", liste_a2[index], liste_b2[index])
print(liste_a2[index] * liste_b2[index])

t2 = time.time()

print("\n", t2-t1)


# cevap: -59231   //// cevap süresi: 4 sn