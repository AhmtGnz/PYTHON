import sqlite3
import time

class Urun():
    def __init__(self, urun_adi, urun_fiyati, kategori, son_kullanma):
        self.urun_adi = urun_adi
        self.urun_fiyati = urun_fiyati
        self.kategori = kategori
        self.son_kullanma = son_kullanma
        
    def __str__(self):
        return "Ürün Bilgileri:\n\nİsim:{}\nFiyatı:\₺{}\nKategori:{}\nSKT:{}\n".format(self.urun_adi, self.urun_fiyati, self.kategori, self.son_kullanma)

class Supermarket():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-11-SQLite/süpermarket.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table if not Exists ürünler (İsim TEXT, Fiyatı TEXT, Kategori TEXT, SKT TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def urun_ekle(self, yeni):
        sorgu = "Insert into ürünler Values(?,?,?,?)"
        self.cursor.execute(sorgu,(yeni.urun_adi, yeni.urun_fiyati, yeni.kategori, yeni.son_kullanma))
        self.baglanti.commit()

    def urunleri_goster(self):
        sorgu = "Select * From ürünler"
        self.cursor.execute(sorgu)
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Ürün Yok!")
        else:
            for i in ürünler:
                ürün = Urun(i[0], i[1], i[2], i[3])
                print(ürün)

    def urun_sorgu(self,urun_adi):
        sorgu = "Select * From ürünler where İsim = ?"
        self.cursor.execute(sorgu,(urun_adi,))
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Bu ürün kayıtlı değil..!")
        else:
            ürün = Urun(ürünler[0][0], ürünler[0][1], ürünler[0][2], ürünler[0][3])
            print(ürün)

    def urun_sil(self):
        urun_adi = input("Silmek İstenen Ürün:")
        sorgu = "Select * From ürünler where İsim = ?"
        self.cursor.execute(sorgu, (urun_adi,))
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Bu ürün zaten Yok..!")
        else:
            cevap = input("Emin misiniz? (E/H)")
            if cevap == "E":
                print("Ürün Siliniyor...")
                time.sleep(1)
                sorgu2 = "Delete From ürünler where İsim = ?"
                self.cursor.execute(sorgu2, (urun_adi,))
                self.baglanti.commit
                print("Ürün silindi..!")

    def kategori_degistir(self, urun_adi):
        sorgu = "Select * From ürünler where İsim = ?"
        self.cursor.execute(sorgu,(urun_adi,))
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Böyle bir ürün bulunamıyor..!")
        else:
            yeni_kategori = input("Yeni kategori:")
            sorgu2 = "Update ürünler set Kategori = ? where İsim = ?"
            self.cursor.execute(sorgu2,(yeni_kategori,urun_adi))
            self.baglanti.commit

            print("Ketegori Güncellendi..!")

    def fiyat_guncelle(self,urun_adi):
        sorgu = "Select * From ürünler where İsim = ?"
        self.cursor.execute(sorgu,(urun_adi,))
        ürünler = self.cursor.fetchall()
        if len(ürünler) == 0:
            print("Böyle bir ürün bulunamıyor..!")
        else:
            yeni_fiyat = float(input("Yeni fiyat:"))
            sorgu2 = "Update ürünler set Fiyatı = ? where İsim = ?"
            self.cursor.execute(sorgu2,(yeni_fiyat,urun_adi))
            self.baglanti.commit

            print("Ürün fiyatı güncellendi..!")

    