"""
If the numbers 1 to 5 are written out in words: 
        one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example,    342 (three hundred and forty-two) contains 23 letters and 
                115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

rakamlar = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
onlular = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
onlar = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
okunuslar = []

for i in range(1,1001):
    if i < 10:
        okunus = rakamlar[i]
        print(okunus)
        okunuslar.append(okunus)
    elif i>=10 and i<20:
        okunus = onlular[i-10]
        print(okunus)
        okunuslar.append(okunus)
    elif i>=20 and i<100:
        if i%10 == 0:
            okunus = onlar[i//10]
            print(okunus)
            okunuslar.append(okunus)
        else:
            okunus = onlar[i//10] + rakamlar[i%10]
            print(okunus)
            okunuslar.append(okunus)
    elif i>=100 and i<1000:
        if i%100 == 0:
            okunus = rakamlar[i//100] + "hundred"
            print(okunus)
            okunuslar.append(okunus)
        elif i%100 >= 10 and i%100 < 20:
            okunus = rakamlar[i//100] + "hundredand" + onlular[(i%100)-10]
            print(okunus)
            okunuslar.append(okunus)
        elif i%100 > 40 and i%100 < 50:
            okunus = rakamlar[i//100] + "hundredandforty" + rakamlar[i%10]
            print(okunus)
            okunuslar.append(okunus)
        elif i%10==0:
            okunus = rakamlar[i//100] + "hundredand" + onlar[(i//10)%10]
            print(okunus)
            okunuslar.append(okunus)
        else:
            okunus = rakamlar[i//100] + "hundredand" + onlar[(i//10)%10] + rakamlar[i%10]
            print(okunus)
            okunuslar.append(okunus)
    else:
        okunuslar.append("onethousand")
        print("onethousand")
uzunluk = 0
for j in okunuslar:
    uzunluk += len(j)

print("toplam uzunluk: ", uzunluk)

"""
cevap 21124
"""