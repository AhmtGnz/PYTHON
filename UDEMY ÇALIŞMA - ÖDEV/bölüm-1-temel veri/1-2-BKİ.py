print("\n\nBeden Kitle Endeksi Bulma\n")
boy = int(input("boyunuz(cm): "))
kilo = int(input("kilonuz: "))
a = int(100)

boym = boy/a

print("beden kitle endeksi: {}\n".format(kilo/boym**2))