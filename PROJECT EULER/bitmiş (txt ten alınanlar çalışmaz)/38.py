"""
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that 
can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


bi sayı al bunu sırayla 1,2,3,.. çarp yanyana yaz. oluşan sayı 9 haneli ve 1den 9a pandijital sayı ise:
seçilen sayıyı ve kaça kadar çarptığını not et: örnek: "192 and (1,2,3) >> 192384576"

bu şekilde yapılabilen en büyük sayı nedir?
"""


def pandigital(sayi):
    a = str(sayi)
    kume = set()
    for i in a:
        kume.add(i)
    if len(kume) == len(a):
        return True
    return False


sayi = 9999
cevap = []
while sayi != 0:
    print(sayi)
    a = str(sayi)
    kontrol = set()
    for x in a:
        kontrol.add(x)
    if len(kontrol) != len(a):
        sayi -= 1
        continue
    for i in range(2,10):
        a += "{}".format(sayi*i)
        if pandigital(int(a)) and len(a) == 9 and "0" not in a:
            cevap.append(int(a))
            print(sayi, i, a)
            break
        elif len(a) > 9:
            break
    sayi -= 1
print(max(cevap))
print(cevap)

# cevap: 932718654
# süre: 1-2 sn

