"""
Problem 4
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
        
        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
        
Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

Not: zip() fonksiyonunu kullanmaya çalışın.
"""


isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
        
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isimler, soyisimler))

for i in liste:
        print(i[0] + " " + i[1])