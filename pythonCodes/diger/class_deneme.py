
class Trial:
    def __init__(self,num1,num2,operation):
        self.num1 = int(input("Sayı 1: "))
        self.num2 = int(input("Sayı 2: "))
        self.operation = int(input("işleminiz: "))

    def sorgu(self):
        self.num1 = int(input("Sayı 1: "))
        self.num2 = int(input("Sayı 2: "))
        self.operation = int(input("işleminiz: "))
    
    def islem(self):
        if self.operation == "*" :
            print("Sonuç: " , (self.num1 + self.num2))

        else:
            print("Yanlış seçim")
                


