def mükemmel(x):

    toplam = 0

    for i in range(1,x):
        if (x % i == 0):
            toplam += i
            
    return toplam

liste = []

for a in range(1,1001):    
    if a == mükemmel(a):
        liste.append(a)

print("1-1000 arası mükemmel sayılar:\n",liste)