birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
yüzler = ["","Yüz","İkiyüz","Üçyüz","Dörtyüz","Beşyüz","Altıyüz","Yediyüz","Sekizyüz","Dokuzyüz"]
binler = ["","Bin","İkibin","Üçbin","Dörtbin","Beşbin","Altıbin","Yedibin","Sekizbin","Dokuzbin"]


sayı1 = int(input("Sayı-1: "))
sayı2 = int(input("Sayı-2: "))

sayı3 = str(sayı1*sayı2)
print(sayı3)

sayı3 = int(sayı3)

bin = sayı3//1000
yüz = (int(sayı3%1000))//100
on = (int(sayı3%100))//10
bir = sayı3%10

print(binler[bin],yüzler[yüz],onlar[on],birler[bir])
