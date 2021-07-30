"""
Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]
     
Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve 
     sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]
     
Not: filter() fonksiyonunu kullanmaya çalışın.
"""


def üçgenmi(tuple):
     k = tuple[0]
     l = tuple[1]
     m = tuple[2]
     if k+l <= m   or   k+m <= l   or   l+m <= k:
          return False
     else:
          return True


denenecek = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(üçgenmi,denenecek)))

