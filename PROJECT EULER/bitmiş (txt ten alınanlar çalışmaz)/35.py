"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

1 milyonun altındaki rakamları yer değişse bile asal sayı olan kaç adet sayı vardır?
"""

import time

t1 = time.time()
def asal_mi(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                return False
        return True

def dongu(sayi):
    a = str(sayi)
    for i in a:
        if int(i)%2 == 0:
            return False       
    if asal_mi(sayi):
        if len(a) == 1:
            return True
        elif len(a) == 2:
            a = a[1] + a[0]
            if asal_mi(int(a)):
                return True
            else:
                return False
        elif len(a) == 3:
            b = a[1] + a[2] + a[0]
            c = a[2] + a[0] + a[1]
            if asal_mi(int(b)) and asal_mi(int(c)):
                return True
            else:
                return False
        elif len(a) == 4:
            b = a[1] + a[2] + a[3] + a[0]
            c = a[2] + a[3] + a[0] + a[1]
            d = a[3] + a[0] + a[1] + a[2]
            if asal_mi(int(b)) and asal_mi(int(c)) and asal_mi(int(d)):
                return True
            else:
                return False
        elif len(a) == 5:
            b = a[1] + a[2] + a[3] + a[4] + a[0]
            c = a[2] + a[3] + a[4] + a[0] + a[1]
            d = a[3] + a[4] + a[0] + a[1] + a[2]
            e = a[4] + a[0] + a[1] + a[2] + a[3]
            if asal_mi(int(b)) and asal_mi(int(c)) and asal_mi(int(d)) and asal_mi(int(e)):
                return True
            else:
                return False
        elif len(a) == 6:
            b = a[1] + a[2] + a[3] + a[4] + a[5] + a[0]
            c = a[2] + a[3] + a[4] + a[5] + a[0] + a[1]
            d = a[3] + a[4] + a[5] + a[0] + a[1] + a[2]
            e = a[4] + a[5] + a[0] + a[1] + a[2] + a[3]
            f = a[5] + a[0] + a[1] + a[2] + a[3] + a[4]
            if asal_mi(int(b)) and asal_mi(int(c)) and asal_mi(int(d)) and asal_mi(int(e)) and asal_mi(int(f)):
                return True
            else:
                return False
    else:
        return False

print("1", "2")
say = 1
for x in range(2,1000000):
    if dongu(x):
        say += 1
        print(say, x)
        
print(say)


t2 = time.time()

print(t2-t1)

# cevap: 55
# süre: 105 sn