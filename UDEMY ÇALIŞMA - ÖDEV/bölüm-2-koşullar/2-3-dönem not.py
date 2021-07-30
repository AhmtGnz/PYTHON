print("Dönem Sonu Harf Notu Hesaplama\n")

vize1 = int(input("İlk vizeden kaç aldın? :"))

if vize1>100:
    print("HATA!! Lütfen Programı Yeniden Başlatın.")

vize2 = int(input("İkinci vizeden kaç aldın?="))

if vize2>100:
    print("HATA!! Lütfen Programı Yeniden Başlatın.")

final = int(input("Finalden kaç aldın?:"))

if final>100:
    print("HATA!! Lütfen Programı Yeniden Başlatın.")


a = vize1 * 0.3
b = vize2 * 0.3
c = final * 0.4

toplam = a+b+c

print("\nToplam Notunuz: {}\n".format(toplam))

if toplam >= 90:
    print("Harf Notunuz: AA")
elif toplam >= 85:
    print("Harf Notunuz: BA")
elif toplam >= 80:
    print("Harf Notunuz: BB")
elif toplam >= 75:
    print("Harf Notunuz: CB")
elif toplam >= 70:
    print("Harf Notunuz: CC")
elif toplam >= 65:
    print("Harf Notunuz: DC")
elif toplam >= 60:
    print("Harf Notunuz: DD")
elif toplam >= 55:
    print("Harf Notunuz: FD")
elif toplam < 55:
    print("Harf Notunuz: FF")