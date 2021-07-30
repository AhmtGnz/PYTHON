birbas = {0:"",1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}
onbas = {0:"",1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan"}

def okunuş(sayı):
    sayı = int(sayı)
    a = sayı % 10
    b = sayı // 10
    print(onbas[b],birbas[a])
    return

sayı = input("sayı:")
okunuş(sayı)