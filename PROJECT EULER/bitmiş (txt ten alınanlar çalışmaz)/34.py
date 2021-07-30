"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""



from math import factorial
cevap = 0
sayi = 3
while sayi<1000000:
    sayi = str(sayi)
    toplam = 0
    for i in sayi:
        toplam += factorial(int(i))

    if int(sayi) == toplam:
        print(sayi)
        cevap += toplam
    sayi = int(sayi)
    sayi += 1
print(cevap)

# cevap: 40730
# süre 1 sn