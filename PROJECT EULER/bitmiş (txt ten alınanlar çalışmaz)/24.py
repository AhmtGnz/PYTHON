"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""


from math import *


sayi = 999999
say0 = 0    #2
say1 = 0    
say2 = 0
say3 = 0
say4 = 0
say5 = 0
say6 = 0
say7 = 0
say8 = 0
say9 = 0

while sayi > 0:
    if sayi >= factorial(9):
        sayi -= factorial(9)
        say0 += 1

    elif sayi < factorial(9) and sayi >= factorial(8):
        sayi -= factorial(8)
        say1 += 1

    elif sayi < factorial(8) and sayi >= factorial(7):
        sayi -= factorial(7)
        say2 += 1

    elif sayi < factorial(7) and sayi >= factorial(6):
        sayi -= factorial(6)
        say3 += 1

    elif sayi < factorial(6) and sayi >= factorial(5):
        sayi -= factorial(5)
        say4 += 1

    elif sayi < factorial(5) and sayi >= factorial(4):
        sayi -= factorial(4)
        say5 += 1

    elif sayi < factorial(4) and sayi >= factorial(3):
        sayi -= factorial(3)
        say6 += 1

    elif sayi < factorial(3) and sayi >= factorial(2):
        sayi -= factorial(2)
        say7 += 1

    elif sayi < factorial(2) and sayi >= factorial(1):
        sayi -= factorial(1)
        say8 += 1
    
print(say0, say1, say2, say3, say4, say5, say6, say7, say8, say9)

a = ["0","1","2","3","4","5","6","7","8","9"]

print(a)

a0 = a[say0]
a.pop(say0)
print(a)

a1 = a[say1]
a.pop(say1)
print(a)

a2 = a[say2]
a.pop(say2)
print(a)

a3 = a[say3]
a.pop(say3)
print(a)

a4 = a[say4]
a.pop(say4)
print(a)

a5 = a[say5]
a.pop(say5)
print(a)

a6 = a[say6]
a.pop(say6)
print(a)

a7 = a[say7]
a.pop(say7)
print(a)

a8 = a[say8]
a.pop(say8)
print(a)

a9 = a[say9]
print(a)

print(int(a0+a1+a2+a3+a4+a5+a6+a7+a8+a9))