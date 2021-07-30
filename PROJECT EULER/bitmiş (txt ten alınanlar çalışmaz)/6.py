toplam = 0
for i in range(1,101):
    toplam += i
toplamın_karesi = toplam**2

kareler_toplamı = 0
liste = [i**2 for i in range(1,101)]
for j in liste:
    kareler_toplamı += j

print("cevap: ",toplamın_karesi-kareler_toplamı)