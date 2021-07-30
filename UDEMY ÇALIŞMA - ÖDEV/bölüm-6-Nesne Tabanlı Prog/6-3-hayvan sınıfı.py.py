class Hayvanlar():
    def __init__(self, beslenme, ortamı, ayak_sayısı, yaş):
        
        self.beslenme = beslenme
        self.ortamı = ortamı
        self.ayak_sayısı = ayak_sayısı
        self.yaş = yaş

    def __str__(self):
        return "Beslenmesi: {}\nYaşama Ortamı: {}\nAyak sayısı: {}\nYaşı: {}\n".format(self.beslenme,self.ortamı,self.ayak_sayısı,self.yaş)

class köpek(Hayvanlar):
    def __init__(self,beslenme, ortamı, ayak_sayısı, yaş, cins):
        super().__init__(beslenme, ortamı, ayak_sayısı, yaş)
        self.cins = cins



class kuş(Hayvanlar):
    def __init__(self,beslenme, ortamı, ayak_sayısı, yaş, cins):
        super().__init__(beslenme, ortamı, ayak_sayısı, yaş)
        self.cins = cins
    def __str__(self):
        return "Beslenmesi: {}\nYaşama Ortamı: {}\nAyak sayısı: {}\nYaşı: {}\nCins: {}".format(self.beslenme,self.ortamı,self.ayak_sayısı,self.yaş,self.cins)
        


class at(Hayvanlar):
    def __init__(self,ayak_sayısı, yaş, yetişme):
        super().__init__(ayak_sayısı, yaş)
        self.yetişme = yetişme

cicikuş = kuş("ay çekirdeği", "evcil", 2, 4, "Cennet Papağanı")

print(cicikuş)





