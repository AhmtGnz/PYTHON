"""
Problem 2

Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 

Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. 

Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. 

Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve 
    liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""
def çiftmi(a):

    if a % 2 == 0:
        return a
    else:
        raise ValueError("Girdiğiniz sayı tek sayıdır.")

liste = [i for i in range(1500,1658)]

for i in liste:
    try:
        print(çiftmi(i))
    except:
        continue