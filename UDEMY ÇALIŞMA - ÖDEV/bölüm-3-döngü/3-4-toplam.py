print("""
*********************
TOPLAM BULMA PROGRAMI
*********************

NOT: Çıkmak için sayı değerini "q" giriniz.
""")

toplam = 0

while True:
    sayı = (input("Sayı:"))
    if sayı == "q":
        break
    else:
        sayı = int(sayı)
        toplam += sayı
print("Toplam:",toplam,"\n")