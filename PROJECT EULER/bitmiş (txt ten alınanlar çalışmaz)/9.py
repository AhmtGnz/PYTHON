
liste = list()

if len(liste)<=2:    
    for i in range(5,1000):
        for j in range(1,i):
            for k in range(1,j):
                if i+j+k == 1000:
                    if ((k**2)+(j**2) == (i**2)):                    
                        liste.append(k)
                        liste.append(j)
                        liste.append(i)

print(liste[0]*liste[1]*liste[2])


