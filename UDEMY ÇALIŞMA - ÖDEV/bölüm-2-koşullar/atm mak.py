print("""
***************
ATM'ye Hoşgeldiniz
***************
""")

print("""

İŞLEMLER:

1 - Bakiye Sorgulama

2 - Para Çekme

3 - Para Yatırma

4 - ATM'den Çıkış

""")

bakiye = 1000

while True:

    işlem = input("İşlem Seçiniz:")

    if işlem == "1":
        print("Bakiyeniz:",bakiye)
    
    elif işlem == "2":
        miktar = int(input("Çekmek İstediğiniz Tutar:"))
        
        if miktar > bakiye:
            print("Bakiyeniz Yetersiz. Lütfen Tekrar Deneyin.")
            continue
        onay = input("Yeni Bakiyeniz {} olacaktır. Onaylıyor musunuz?".format(bakiye-miktar))
        if onay == "evet":
            bakiye -= miktar
            print("Para Çekme İşlemi Tamamlandı.\nKalan Bakiyeniz: {} TL'dir.".format(bakiye))
        else:
            print("Yeniden Deneyiniz.")
  
    elif işlem == "3":
        miktar = int(input("Yatırmak İstediğiniz Tutar:"))
        bakiye += miktar
        print("Yeni Bakiyeniz: ",bakiye)

    elif işlem == "4":
        print("Yine Bekleriz..")
        break

    else:
        print("Geçersiz İşlem..")