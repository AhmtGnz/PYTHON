import time
import random



class Bilgisayar():

    def __init__(self,marka,ram,ekran_kartı,harddisk_kapasitesi = 1028,harddisk_türü = "HDD"):
        self.marka = marka
        self.ram = ram
        self.ekran_kartı = ekran_kartı
        self.harddisk_kapasitesi = harddisk_kapasitesi
        self.harddisk_türü = harddisk_türü

    def __str__(self):
        return f"Marka: {self.marka}\nRam: {self.ram}\nEkran Kartı: {self.ekran_kartı}\nHarddisk: {self.harddisk_türü}\nHarddisk Kapasitesi: {self.harddisk_kapasitesi}"

    def __len__(self):
        print("Harddisk Kapasitesi: {}\nRam: {}\nEkran Kartı: {}".format(self.harddisk_kapasitesi,self.ram,self.ekran_kartı))

    def harddisk_ekle(self):
        yeni_harddisk = input("HDD mi SSD mi?\t")
        yeni_boyut = int(input("Kaç GB?\t"))

        if yeni_harddisk == "SSD":
            self.harddisk_türü = "HDD + SSD"
        
        self.harddisk_kapasitesi += yeni_boyut
        print("Yeni Boyut: {}".format(self.harddisk_kapasitesi))

    def ram_ekle(self):
        yeni_ram = int(input("Eklenecek Ram Boyutu: "))
        self.ram += yeni_ram
        print("Yeni RAM: {}".format(self.ram))

    def ekran_kartı_ekle(self):
        yeni_ekran =int(input("Eklenecek Ekran Kartı boyutu: "))
        self.ekran_kartı += yeni_ekran
        print("Yeni Ekran Kartı Boyutu: {}".format(self.ekran_kartı))    



Ahmetin_bilgisayarı = Bilgisayar("MSİ",16,2,1028,"HDD + SSD")

print("""
Bilgisayar Uygulaması

İŞLEMLER:

1. Harddisk Ekle
2. RAM ekle
3. Ekran Kartı Ekle

NOT: Çıkmak için 'q' basıp onaylayın.

""")


while True:
    işlem = input("İşlem Seçiniz:\t")

    if işlem == "q":
        print("Çıkış yapıldı.  Yine Bekleriz...")
        break

    elif işlem == "1":
        Ahmetin_bilgisayarı.harddisk_ekle()

    elif işlem == "2":
        Ahmetin_bilgisayarı.ram_ekle()

    elif işlem == "3":
        Ahmetin_bilgisayarı.ekran_kartı_ekle()

    else:
        print("Geçersiz İşlem Girdiniz. Lütfen 1, 2, 3 yazın yada çıkmak için 'q' yazıp onaylayın.")

    