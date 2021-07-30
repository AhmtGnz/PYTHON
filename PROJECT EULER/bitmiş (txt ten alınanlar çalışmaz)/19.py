"""
You are given the following information, but you may prefer to do some research for yourself.

>> 1 Jan 1900 was a Monday.

>> Thirty days has September, April, June and November.
    30 gün: Nisan, Haziran, Eylül ve Kasım

>> All the rest have thirty-one,
    Geri kalan aylar Şubat hariç 31 gün

>> Saving February alone, Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

>> A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.


>> How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
20. yüzyılda pazar günü kaç kere ayın birine denk gelmiştir? 
"""


aylar = ["ocak", "subat", "mart", "nisan", "mayıs", "haziran", "temmuz", "agustos", "eylül", "ekim", "kasım", "aralık"]
günler = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]
yıl = 1901
ay_say = 1
say = 0
cevap = 0
gün_say = 2   

while yıl <= 2000:
    say += 1
    ay = aylar[(ay_say%12)-1]
    gün = günler[(gün_say%7)-1] 
    gün_say += 1
    
    if ay == "ocak" or ay == "mart" or ay == "mayıs" or ay == "temmuz" or ay == "agustos" or ay == "ekim":
        if say == 31:
            say = 0
            ay_say += 1

    elif ay == "subat":
        if yıl%4 == 0 and yıl != 1900:
            if say == 29:
                say = 0
                ay_say += 1
        else:
            if say == 28:
                say = 0
                ay_say += 1
        
    elif ay == "aralık":
        if say == 31:
            say = 0
            ay_say += 1
            yıl += 1

    else:
        if say == 30:
            say = 0
            ay_say += 1

    if gün == "pazar" and say == 1:
        cevap += 1

   
print(cevap)




