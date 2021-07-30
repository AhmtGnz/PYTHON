"""
Proje 1
Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın 
ve bunların nerede bulunduklarını ve isimlerini ayrı ayrı 
"pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin.
"""



import os

with open("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-14-ileri seviye moduller/pdf_dosyaları.txt","w",encoding="utf-8") as pdf:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("E:"):
        for i in dosya_isimleri:
            if (i.endswith(".pdf")):
                pdf.write(i + "\n")

with open("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-14-ileri seviye moduller/mp4_dosyaları.txt","w",encoding="utf-8") as mp4:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("E:"):
        for i in dosya_isimleri:
            if (i.endswith(".mp4")):
                mp4.write(i + "\n")

with open("g:/PYTHON/UDEMY ÇALIŞMA - ÖDEV/bölüm-14-ileri seviye moduller/txt_dosyaları.txt","w",encoding="utf-8") as txt:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("E:"):
        for i in dosya_isimleri:
            if (i.endswith(".txt")):
                txt.write(i + "\n")