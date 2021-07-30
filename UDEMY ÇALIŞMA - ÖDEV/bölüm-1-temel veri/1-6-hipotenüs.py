print("\n\nHipotenüs Bulma\n")

print("aklınıza bir dik üçgen getirin ve dik kenarlarına a ve b diyin\n")

print("şimdi bana a değerini söyleyin: ")

a = int(input("a: "))

print("\nşimdi de b değerini söyleyin: ")

b = int(input("b: "))

c = a**2 + b**2
d = c**0.5


print("\nşimdi ben size son kenarın(hipotenüs=c) uzunluğunu söyleyeyim: ")

print("c: {}\n".format(d))