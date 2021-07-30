print("""
****************************
MÜKEMMEL SAYI BULMA PROGRAMI
****************************

NOT: Programdan çıkmak için sayı değerini q giriniz.
""")

while True:

    x = input("Sayı: ")

    if x == "q":
        print("Program sonlandı.\n")
        break
     
    else:
        x = int(x)
        liste = [*range(1,x)]
        liste2 = []

        for i in liste:
            if x % i == 0:
                liste2.append(i)
        print(liste2,"\n")
        
        toplam = 0

        for j in liste2:
            toplam += j

        if x == toplam:
            print("{} bir mükemmel sayıdır.\n".format(x))
        else:
            print("{} mükemmel sayı değildir.\n".format(x))