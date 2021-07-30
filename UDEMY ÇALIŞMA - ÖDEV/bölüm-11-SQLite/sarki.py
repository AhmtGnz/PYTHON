import sqlite3

import time

class Sarki():
    def __init__(self, sarki_adi, sanatci, sarki_uzunlugu, album, produksiyon):
        self.sarki_adi = sarki_adi
        self.sanatci = sanatci
        self.sarki_uzunlugu = sarki_uzunlugu
        self.album = album
        self.produksiyon = produksiyon
        
    def __str__(self):
        return "\nŞarkı Adı:\t{}\nSanatçı:\t{}\nŞarkı Uzunluğu:\t{}\nAlbüm:\t{}\nProdüksiyon:\t{}\n".format(self.sarki_adi, self.sanatci, self.sarki_uzunlugu, self.album, self.produksiyon)


class Sarki_Kutuphanesi():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-11-SQLite/Şarkı Kütüphanesi.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "create table if not exists sarkilar (Sarki_Adi TEXT, Sanatci TEXT, Sarki_Uzunlugu TEXT, Album TEXT, Produksiyon TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit

    def baglanti_kes(self):
        self.baglanti.close

    def sarki_sorgula(self,sarki_adi):
        sorgu = "Select * From sarkilar where Sarki_Adi = ?"
        self.cursor.execute(sorgu,(sarki_adi,))
        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("Bu Şarkı Kayıtlı Değil!")
        else:
            sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4])
            print(sarki)

    def sarkilari_goster(self):
        sorgu = "Select * From sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("Kayıtlı Şarkı Yok!")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_ekle(self, sarki):

        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.sarki_adi, sarki.sanatci, sarki.sarki_uzunlugu, sarki.album, sarki.produksiyon))

        self.baglanti.commit()

    def sarki_sil(self, sarki_adi):
        sorgu1 = "Delete From sarkilar where Sarki_Adi = ?"

        self.cursor.execute(sorgu1,(sarki_adi,))

        self.baglanti.commit()

    def toplam_uzunluk(self):
        sorgu = "Select * From sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if len(sarkilar)==0:
            print("Şarkı Yok!")
        else:
            toplam_dakika = 0
            toplam_saniye = 0
            for i in sarkilar:
                a = i[2]
                b = a.split(":")
                toplam_dakika += int(b[0])
                toplam_saniye += int(b[1])
            dakika = toplam_dakika + toplam_saniye//60
            saniye = toplam_saniye % 60
            print("Toplam Şarkı Uzunluğu: {} dakika {} saniye".format(dakika, saniye))

    
