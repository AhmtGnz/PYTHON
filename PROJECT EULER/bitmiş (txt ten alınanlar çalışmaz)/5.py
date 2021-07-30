asal = []
çarpım = 1
for i in range(2,21):    # Asal Çarpanları Listeleme
    bolundu = False
    for j in range(2,i):
        if i%j == 0:
            bolundu = True
            break
        else:
            continue
    if bolundu == False:
        asal.append(i)
            
for x in asal:   # Asal çarpan listesi içindekileri çarpma
    çarpım *= x

for y in range(2,21):  # Bölünmeyenleri ekleme
    if çarpım % y == 0:
        continue
    else:
        for z in asal:
            if y % z == 0:
                y = y/z
        asal.append(y)

cevap = 1
for t in asal:
    cevap *= t
print(int(cevap))