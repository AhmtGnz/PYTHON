"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
            
            
Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.
"""



a = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


harfler = dict()


for i in a:

    if (i in harfler):
        harfler[i] += 1

    else:
        harfler[i] = 1

for kelime,sayı in harfler.items():

    print("{} harfi {} defa geçiyor....".format(kelime,sayı))

    print("---------------------------")