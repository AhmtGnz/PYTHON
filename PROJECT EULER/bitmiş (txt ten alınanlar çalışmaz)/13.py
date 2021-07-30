"""
Soru 13.txt dosyasında..
kod ile açıldı..

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""



with open("G:/PYTHON/PROJECT EULER/13.txt","r",encoding="utf-8") as file:
    a = file.read()
    liste = a.split("\n")

toplam = 0
for i in range(0,len(liste)):
    toplam += int(liste[i])

toplam = str(toplam)

print("cevap: ", toplam[:10])