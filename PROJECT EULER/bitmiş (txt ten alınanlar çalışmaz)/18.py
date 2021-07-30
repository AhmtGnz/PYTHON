import time
t1 = time.time()



with open("G:/PYTHON/PROJECT EULER/18.txt","r",encoding="utf-8") as file:
    a = file.read()
    liste = a.split("\n")

satırlar = []
deger = 0
while len(satırlar) < len(liste):
    satır = liste[deger]
    satır = satır.split(" ")
    satırlar.append(satır)
    deger += 1

for i in range(0,len(satırlar)):
    for j in range(0,len(satırlar[i])):
        satırlar[i][j] = int(satırlar[i][j])
        
while len(satırlar)!=1:
    for x in range(0,len(satırlar[-2])):
        if satırlar[-1][x] > satırlar[-1][x+1]:
            satırlar[-2][x] += satırlar[-1][x]
          
        else:
            satırlar[-2][x] += satırlar[-1][x+1]
           
    satırlar.pop()


print(satırlar[0][0])





t2 = time.time()

print("Geçen süre: ", t2-t1, "saniye")