"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


import time
t1 = time.time()

cevap_kumesi = set()
for i in range(100):
    for j in range(i,2000):
        c = i*j
        d = str(i)+str(j)+str(c)
        if len(d) == 9 and "0" not in d:
            kume = set()
            for a in d:
                kume.add(a)
            if len(kume) == 9:
                print(i, "x", j, "=", c)
                cevap_kumesi.add(c)
print("\n", cevap_kumesi, "\n", sum(cevap_kumesi))


t2 = time.time()
print(t2-t1)

# cevap: 45228
# süre: 0,22 sn