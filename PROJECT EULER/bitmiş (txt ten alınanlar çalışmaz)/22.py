"""
Using 22.txt, 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

dosyayı alfabetik sırala.
isimlerin kaçıncı sırada olduğunu bul
her isimin harflerinin alfabede kaçıncı olduklarını bulup topla.
bulduğun iki sayıyı çarp.
sonuç ismin puanı oldu

tüm isimlerin puanlarının toplamı kaç?

a b c d e f g h i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""

harfler = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}


with open("g:/PYTHON/PROJECT EULER/22.txt","r",encoding="utf-8") as file:

    a = file.read()
    liste = a.split(",")

liste2 = []
for i in liste:
    liste2.append(i[1:-1])

print(liste2)
liste2.sort()
print(liste2)

cevap = []
for i in range(0,len(liste2)):
    isim = liste2[i]
    toplam = 0
    for j in isim:
        toplam += harfler[j]

    cevap.append(toplam*(i+1))

print(sum(cevap))