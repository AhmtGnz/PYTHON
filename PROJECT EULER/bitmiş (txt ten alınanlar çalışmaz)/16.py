"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

kacinci_kuvvet = 1000

a = str(2**kacinci_kuvvet)
toplam = 0
for i in a:
    toplam += int(i)
print(toplam)