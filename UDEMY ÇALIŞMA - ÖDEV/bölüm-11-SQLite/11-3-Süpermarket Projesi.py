"""
Proje 3
Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın.
"""



print("""


SÜPERMARKET'e Hoşgeldiniz..!

Yapılabilecek İşlemler:

1 - Ürün Listeleme

2 - Ürün Ekleme
        NOT: Eğer fiyat küsüratlı ise '.' ile ayırın. Örnek: '156.48'

3 - Ürün Silme

4 - Ürün Sorgulama

5 - Kategori Değiştirme

6 - Fiyat Güncelleme
        NOT: Eğer yeni fiyat küsüratlı ise '.' ile ayırın. Örnek: '156.48'

Çıkmak için "q" basıp onaylayın.

""")



from süpermarket import *

supermarket = Supermarket()

while True:
    işlem = input("\nİşlem Seçiniz:")
    if işlem == "q":
        print("Bye Bye")

    elif işlem == "1":
        supermarket.urunleri_goster()

    elif işlem == "2":   
        urun_adi = input("Yeni Ürün Adı:")
        urun_fiyati = input("Fiyat:")
        kategori = input("Kategori:")
        son_kullanma = input("Son Kullanma Tarihi:")
        
        yeni = Urun(urun_adi, urun_fiyati, kategori, son_kullanma)

        print("Ürün ekleniyor..")
        time.sleep(1)
        supermarket.urun_ekle(yeni)
        print("Ürün Eklendi..")

    elif işlem == "3":
        supermarket.urun_sil()

    elif işlem == "4":
        urun_adi = input("Hangi Ürünü Arıyorsun?")
        supermarket.urun_sorgu(urun_adi)

    elif işlem == "5":
        ürün = input("Hangi ürünün kategorisini değiştirmek istiyorsun:")
        supermarket.kategori_degistir(ürün)

    elif işlem == "6":
        ürün = input("Hangi Ürünün Fiyatı Değişecek?")
        supermarket.fiyat_guncelle(ürün)

    else:
        print("Geçersiz Giriş. Tekrar Deneyin..!")