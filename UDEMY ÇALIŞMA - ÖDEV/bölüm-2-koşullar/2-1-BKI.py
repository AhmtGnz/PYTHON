print("Beden Kitle Endeksi(BKI) Hesaplama Programı'na Hoşgeldiniz...\n")

"""
BKİ : kilo (kg) / boy (m) * boy (m)

BKİ<18.5  : zayıf
18.5< BKI < 25  : normal
25< BKI < 30  : fazla kilolu
30< BKI  : obez
"""

print("Bana kilo ve boy bilgilerinizi verin.\nBen size Beden Kitle Endeksinizi hesaplayıp kilo durumunuzu söyleyeyim.")

boy = int(input("Boyunuz (cm) :"))
kilo = int(input("Kilonuz (kg) :"))

mboy = boy / 100

BKI = kilo / (mboy * mboy)

print("Beden Kitle Endeksiniz: {} dir.".format(BKI))

if (BKI < 18.5):
    print("Zayıfsınız. ")
elif BKI < 25:
    print("Normal")
elif BKI < 30:
    print("Fazla kilolusunuz.")
else:
    print("Obez'siniz.")
