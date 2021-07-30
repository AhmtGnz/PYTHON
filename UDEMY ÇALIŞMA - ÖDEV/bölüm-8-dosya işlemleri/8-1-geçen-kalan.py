"""
Proje 1
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları 
    "kalanlar.txt" dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.
"""

def not_hesapla(satır):


    satır = satır[:-1]

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    liste = [isim, son_not, harf]

    return liste

with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/dosya.txt","r",encoding= "utf-8") as file:
    kalanlar = []
    geçenler = []

    for i in file:

        liste = not_hesapla(i)

        if liste[-1] == "FF" or liste[-1] == "FD" or liste[-1] == "DD" or liste[-1] == "DC":
            kalanlar.append(liste[0] + "  > > >  " + liste[-1] + "\n")

        else:
            geçenler.append(liste[0] + "  > > >  " + liste[-1] + "\n")

    with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/kalanlar.txt","w",encoding="utf-8") as file2:
        file2.writelines(kalanlar)

    with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/geçenler.txt","w",encoding="utf-8") as file3:
        file3.writelines(geçenler)

