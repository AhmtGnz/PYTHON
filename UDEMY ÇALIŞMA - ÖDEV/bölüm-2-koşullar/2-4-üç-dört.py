print("Üçgen - Dörgen Problemi\n")

ne = input("Üçgen mi Dörtgen mi?:")

if ne=="üçgen" or ne=="Üçgen" or ne=="üç":
    k = int(input("ilk kenar uzunluğu:"))
    l = int(input("ikinci kenar uzunluğu:"))
    m = int(input("üçüncü kenar uzunluğu:"))

    if k+l < m or k+m < l or l+m < k:
        print("İmkansız Üçgen")
    elif k==l and k==m:
        print("Eşkenar Üçgen")
    elif k==l or k==m or l==m:
        print("İkizkenar Üçgen")
    else:
        print("Normal Üçgen")

elif ne=="dörtgen" or ne=="dört" or ne=="Dörtgen":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))

    if a==b and a==c and a==d:
        print("Kare")
    elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        print("Dikdörtgen")
    elif (a>b+c+d) or (b>a+c+d) or (c>a+b+d) or (d>a+b+c):
        print("İmkansız Dörtgen")
    else:
        print("Sıradan Dörtgen")
else:
    print("Yanlış giriş yaptınız!")