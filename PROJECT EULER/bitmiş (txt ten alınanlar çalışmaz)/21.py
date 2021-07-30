"""
Let d(n) be defined as the sum of proper divisors of n 
    (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
    each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def dostane_mi(x):
    liste = []
    for i in range(1,int(x/2)+1):
        if x % i == 0:
            liste.append(i)
    toplam = 0            
    for j in liste:
        toplam += j

    liste2 = []
    for k in range(1,int(toplam/2)+1):
        if toplam%k == 0:
            liste2.append(k)

    toplam2 = 0
    for a in liste2:
        toplam2 += a

    if toplam2 == x and x != toplam:
        print(x, toplam)
        return True
    else:
        return False

dostane_listesi = []
for i in range(2,10000):
    if dostane_mi(i):
        dostane_listesi.append(i)

cevap = 0
for y in dostane_listesi:
    cevap += y

print(cevap)