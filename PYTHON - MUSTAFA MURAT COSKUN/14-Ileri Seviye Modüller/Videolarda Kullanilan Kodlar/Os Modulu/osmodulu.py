import os
from datetime import datetime


for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Kullanıcılar/ahmet/Masaüstü"):
    for i in dosya_isimler:
        if i.endswith(".xlsx"):
            print(i)

# DERS NOTLARI


# print(dir(os))

# print(os.getcwd())                            >>  çalışılan dosyanın hangi dizinde oldugunu söyler.

# os.chdir("C:/Users/user/Desktop/")            >>  çalışmak istenilen dizine gider.

# print(os.listdir())                           >>  çalışılan dosyanın bulundugu dizindeki tüm dosyaları listeler

# os.mkdir("Deneme1")                           >>  yeni dizin oluşturur (bulunulan klasöre alt klasör ekler)

# os.makedirs("Deneme2/Deneme3")                >>  bulunulan klasöre belirtilen dizini ekler

# os.rmdir("Deneme2/Deneme3")                   >>  "deneme3" klasörünü siler.

# os.removedirs("Deneme2/Deneme3")              >>  belirtilen dizin komple silinir.

# os.rename("Deneme1","Deneme2")                >>  klasör adını değiştirir

# os.rename("test.txt","test2.txt")             >>  dosya adını değiştirir

# print(os.stat("test2.txt"))                   >>  belirtilen dosyanın tüm özelliklerini verir

# degistirilme = os.stat("test2.txt").st_mtime  >>  dosya özelliklerinden st_mtime özelliğini verir (değiştirme zamanı sn olarak)

# print(datetime.fromtimestamp(degistirilme))   >>  sn yi normal tarihe çevirir. (bir önceki ders)


"""for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):
                                                >>  os.walk > belirtilen dizin altındaki tüm dosyaları listeler.
                                                                liste 3 elemanlı demetleri listeler.
                                                                demetin     birinci elemanı: dizini
                                                                            ikinci eleman: klasörleri
                                                                            üçüncü eleman: dosyaları

    print("Current Path",klasör_yolu)
    print("Directories",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")"""





