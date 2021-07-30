import math
import time

print("""
***************
HESAP MAKİNESİ
***************
""")

print("""

İŞLEMLER:

1 - Toplama

2 - Çıkarma

3 - Çarpma

4 - Bölme

5 - Kök Alma

6 - Yüzde Alma

7 - Trigonometri
   
8 - Faktöriyel Alma

9 - Logaritma

10 - Çıkış

""")


while True:

    işlem = input("İşlem Seçiniz:")

    # Çıkış.
    if işlem == "10":
        print("\nÇıkış Yapılıyor.")
        print("\n")
        time.sleep(1)
        break
    

    # Toplama
    elif işlem == "1":
        print("\nToplama İşlemi Seçildi\n")
        time.sleep(1)
        print("Toplamak İstediğiniz Değerleri Giriniz.\n")
        a = int(input("a:"))
        b = int(input("b:"))
        print("\n")
        print(f"{a}+{b}=",a+b)
        print("\n")
        

    # Çıkarma
    elif işlem == "2":
        print("\nÇıkarma İşlemi Seçildi\n")
        time.sleep(1)
        a = int(input("a-b işleminde 'a' değeri:"))
        b = int(input("a-b işleminde 'b' değeri:"))
        print("\n")
        print(f"{a}-{b}=",a-b)
        print("\n")
        

    # Çarpma
    elif işlem == "3":
        print("\nÇarpma İşlemi Seçildi\n")
        time.sleep(1)
        print("Çarpmak İstediğiniz Değerleri Giriniz.\n")
        a = int(input("a:"))
        b = int(input("b:"))
        print("\n")
        print(f"{a}*{b}=",a*b)
        print("\n")
        

    # Bölme
    elif işlem == "4":
        print("\nBölme İşlemi Seçildi\n")
        time.sleep(1)
        a = int(input("a/b işleminde 'a' değeri:"))
        b = int(input("a/b işleminde 'b' değeri:"))
        print("\n")
        print(f"{a}/{b}=",a/b)
        print("\n")


    # Kök Alma
    elif işlem == "5":
        print("\nKök Alma İşlemi Seçildi")
        time.sleep(1)
        print("""
        1 - Karekök almak istiyorum.
        2 - Küp kök almak istiyorum.
        3 - Kaçıncı kök olduğunu belirtmek istiyorum.        
        """)

        giriş = input("Hangisi? >>> ")

        if giriş == "1":
            sayı = int(input("\nSayıyı Giriniz="))
            print("\n")
            print(f"kök {sayı} =",sayı ** 0.5)
            print("\n")

        elif giriş == "2":
            sayı = int(input("\nSayıyı Giriniz="))
            print("\n")
            print("küpkök {} =".format(sayı),sayı ** (1/3))
            print("\n")

        elif giriş == "3":
            sayı = int(input("\nSayıyı Giriniz="))
            kök = int(input("kaçıncı kök?"))
            print("\n")
            print(f"{sayı} sayısının {kök}. kökü=",sayı ** (1/kök))
            print("\n")

        else:
            print("\nGeçersiz Giriş!")
            print("\n")
        

    # Yüzde Alma
    elif işlem == "6":
        print("\nYüzde Alma İşlemi Seçildi\n")
        time.sleep(1)
        a = int(input("Yüzdesi alınacak sayı:"))
        b = int(input("Yüzde kaçı:"))
        print(f"\n{a}'nın yüzde {b}si=",(a*b)/100)
        print("\n")
        

    # Trigonometri
    elif işlem == "7":
        print("\nTrigonometri İşlemi Seçildi")
        time.sleep(1)
        print("""
        7-1 - Sinüs
        7-2 - Cosinüs
        7-3 - Tanjant
        7-4 - Cotanjant
        """)

        giriş = input("Hangisi >>>")

        if giriş == "1":
            sayı = int(input("\nAçıyı Giriniz = "))
            print("\nsin({}) =".format(sayı),math.sin(sayı))
        
        elif giriş == "2":
            sayı = int(input("\nAçıyı Giriniz = "))
            print("\ncos({}) =".format(sayı),math.cos(sayı))
        
        elif giriş == "3":
            sayı = int(input("\nAçıyı Giriniz = "))
            print("\ntan({}) =".format(sayı),math.tan(sayı))
        
        elif giriş == "4":
            sayı = int(input("\nAçıyı Giriniz = "))
            print("\ncot({}) =".format(sayı),1/math.tan(sayı))
        
        else:
            print("\nGeçersiz Giriş!")
        print("\n")
        

    # Faktöriyel
    elif işlem == "8":
        print("\nFaktöriyel İşlemi Seçildi\n")
        time.sleep(1)
        sayı = int(input("Sayı:"))
        print(f"\n{sayı}!=",math.factorial(sayı))
        print("\n")
        

    # logaritma
    elif işlem == "9":
        print("\nlogaritma İşlemi Seçildi\n")
        time.sleep(1)
        sayı = int(input("log(x) için x sayısı giriniz:"))
        print(f"\nlog({sayı})=",math.log(sayı))
        print("\n")
        

    else:
        print("\nGeçersiz Giriş!")
        break