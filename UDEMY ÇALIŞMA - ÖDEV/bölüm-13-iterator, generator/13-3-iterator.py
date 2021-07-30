"""
Program 1
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. 
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve 
her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. 
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""


class Kareler():
    def __init__(self,max = 0):
        self.max = max
        self.sayi = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi < self.max:
            self.sayi += 1
            return self.sayi ** 2
        self.sayi = 0
        raise StopIteration
        
kareler = Kareler(20)

for i in kareler:
    print(i)