"""
Proje 2
Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;
                     
                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi
                     
                     Örnek Metodlar;
                     
                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil
                     
"""





from sarki import *

print("""***********************************

Şarkı Kütüphanesi Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Sorgulama

3. Şarkı Ekle

4. Şarkı Sil 

5. Toplam Şarkı Uzunluğu

Çıkmak için 'q' ya basın.
***********************************""")

sarki_kutuphanesi = Sarki_Kutuphanesi()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    
    elif (işlem == "1"):
        sarki_kutuphanesi.sarkilari_goster()
        
    elif (işlem == "2"):
        isim = input("Şardı Adını Giriniz:\t")
        print("Şarkı Sorgulanıyor...")
        time.sleep(2)
        sarki_kutuphanesi.sarki_sorgula(isim)

    elif (işlem == "3"):
        sarki_adi = input("Şarkı Adı:\t")
        sanatci = input("Sanatçı:\t")
        sarki_uzunlugu = input("Şarkı Uzunluğu (Örnek: '03:26' Şeklinde giriniz):\t")
        album = input("Albüm:\t")
        produksiyon = input("Prodüksiyon:\t")

        yeni_sarki = Sarki(sarki_adi, sanatci, sarki_uzunlugu, album, produksiyon)
        print("Şarkı ekleniyor....")
        time.sleep(2)
        sarki_kutuphanesi.sarki_ekle(yeni_sarki)
        print("Şarkı Eklendi....")

    elif (işlem == "4"):
        
        sarki_adi = input("Silinecek Şarkı Adı:\t")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Şarkı Siliniyor...")
            time.sleep(2)
            sarki_kutuphanesi.sarki_sil(sarki_adi)
            print("Şarkı silindi....")

    elif (işlem == "5"):
        sarki_kutuphanesi.toplam_uzunluk()

    else:
        print("Geçersiz İşlem...")
