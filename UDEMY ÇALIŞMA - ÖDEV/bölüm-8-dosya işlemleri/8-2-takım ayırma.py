"""
Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine 
    Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. 
    Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""


def takım_ayırma(satır):
    satır = satır[:-1]

    liste = satır.split(",")

    gs = []
    fb = []
    bjk = []

    if liste[1] == "Galatasaray":
        gs.append(liste[0] + "\n")

    elif liste[1] == "Fenerbahçe":
        fb.append(liste[0] + "\n")
    
    elif liste[1] == "Beşiktaş":
        bjk.append(liste[0] + "\n")
    
    with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/gs.txt","a",encoding="utf-8") as GS:
        GS.writelines(gs)

    with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/fb.txt","a",encoding="utf-8") as FB:
        FB.writelines(fb)

    with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/bjk.txt","a",encoding="utf-8") as BJK:
        BJK.writelines(bjk)

with open("d:/YAZILIM/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-8-dosya işlemleri/futbolcular.txt","r",encoding="utf-8") as file:
    

    for i in file:
        takım_ayırma(i)
