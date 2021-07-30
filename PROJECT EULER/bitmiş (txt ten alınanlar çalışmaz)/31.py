"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time

t1 = time.time()

say = 1

for i in range(3):
    for j in range(5):
        print(i, j)
        for x in range(11):
            for y in range(21):
                for z in range(41):
                    for k in range(101):
                        toplam = i*100 + j*50 + x*20 + y*10 + z*5 + k*2
                        if toplam <= 200:
                            say += 1
                        else:
                            break

print(say)

t2 = time.time()
print(t2-t1)

# cevap: 73682
# süre: 0,1 sn