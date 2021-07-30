"""
Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
"""


def asal_mi(sayı):
    if sayı == 2:
        return True
    elif sayı == 1:
        return False
    else:
        for i in range(2,sayı):
            if (sayı % i == 0):
                return False
        return True
            
def asal():
    x = 2

    while True:
        if asal_mi(x):
            yield x
        x += 1



for sayı in asal():
    if sayı > 1000:
        break
    print(sayı)