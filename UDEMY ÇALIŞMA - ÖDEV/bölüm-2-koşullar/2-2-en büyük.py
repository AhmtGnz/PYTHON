print("Girilen Üç Sayıdan En Büyüğünü Bulma")

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

if (a < c and b < c):
    print("c={} en büyüktür.".format(c))
elif (b < a and c < a):
    print("a={} en büyüktür.".format(a))
elif (a < b and c < b):
    print("b={} en büyüktür.".format(b))
else:
    print("Hepsi eşit.")