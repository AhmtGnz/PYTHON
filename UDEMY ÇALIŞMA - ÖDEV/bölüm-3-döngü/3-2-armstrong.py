print("""
******************************

ARMSTRONG SAYI KONTROL PROGRAMI

******************************

NOT: Programdan çıkmak için değeri "q" giriniz.
""")

while True:
    sayı = input("\nSayı: ")

    if sayı == "q":
        print("Programdan çıkıldı.")

    else:
        a = len(sayı)
        print("Sayı uzunluğu:",a)
        liste = []
        
        for i in sayı:
            i = int(i)
            j = i**a
            liste.append(j)
        print(liste)
        toplam = 0
        
        for k in liste:
            toplam += k
        print("Toplam: ",toplam)

        sayı = int(sayı)

        if sayı == toplam:
            print("Harika! Bir Armstrog Sayı Buldunuz!")
        else:
            print("{} bir armstrong sayı değildir.".format(sayı))