"""
The fraction 49/98 is a curious fraction, 
as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

Demiş ki 49/98 ile 4/8 eşit. Ama bunu sanki pay ve paydadaki 9lar 
birbirini götürür şeklinde yanlış bı matematik işlemi yaparsan da sonuç doğru çıkıyor. 
Bu şekilde sonu sıfırlı olanlari saymazsak, payı paydası iki basamaklı ve sonucu 1den küçük sadece 4 tane kesir varmış. 
Bunları çarp ve en sadelesmis halinin paydasini bana ver demiş...
"""


bolen = 1
cevap = 1

for i in range(11,99):
    for j in range(i,100):
        a = str(i)
        b = str(j)
        if a[0] == b[0]:
            a = int(a[1])
            b = int(b[1])
        elif a[0] == b[1]:
            a = int(a[1])
            b = int(b[0])            
        elif a[1] == b[0]:
            a = int(a[0])
            b = int(b[1])            
        elif a[1] == b[1]:
            a = int(a[0])
            b = int(b[0])
        else:
            a = int(a)
            b = int(b)            

        if b != 0 and i/j == a/b and i/j < 1 and i != a and i%10 != 0:
            print(f"{i} / {j} = {a} / {b}")
            cevap *= b
            bolen *= a

if cevap%bolen == 0:
    cevap /= bolen

print(cevap)

# cevap: 100
# süre: <1 sn