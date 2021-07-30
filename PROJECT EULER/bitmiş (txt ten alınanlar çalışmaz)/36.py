"""
Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

1 milyonun altındaki sayılardan hem 10 hemde 2 tabanında palindromik olan sayıları bul topla.
"""

def palindrom(sayi):
    a = int(str(sayi)[::-1])
    if a == sayi:
        return True
    return False

def taban_iki(sayi):
    ikili = ""
    while sayi != 0:
        ikili += f"{sayi%2}"
        sayi = sayi//2              
    return ikili[::-1]

say = 0
cevap = 0
for on in range(1,1000000):
    iki = taban_iki(on)
    if palindrom(on) and palindrom(int(iki)):
        say += 1
        print(say, on , iki)
        cevap += on

print(cevap)

# cevap: 872187
# süre: 2 sn