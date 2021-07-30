"""
Program
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. 
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 
1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.
"""


from time import perf_counter


def mükemmel(func):
    def wrapper(kaça_kadar):
        ne = range(kaça_kadar)
        mükemmeller = []
        for x in ne:
            liste = [*range(1,x)]
            liste2 = []
            for i in liste:
                if x % i == 0:
                    liste2.append(i)
            
            toplam = 0
            for j in liste2:
                toplam += j

            if x == toplam:
                mükemmeller.append(x)

        print("mükemmel sayılar:\n", mükemmeller)

        func(kaça_kadar)
    
    return wrapper

@mükemmel
def asal(kaça_kadar):
    
    asal = [2]

    a = 3

    while a <= kaça_kadar:
        
        for i in asal:
            bolundu = False
            if a%i == 0:
                bolundu = True
                break
            else:
                continue
        if bolundu == False:
            asal.append(a)
            
        
        a += 2

    print("\nasal sayılar:\n", asal)

asal(1000)
