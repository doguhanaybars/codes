import random

sayı = random.randint(0, 100)

hak = int(input("Kaç hakkınız olduğunu giriniz: "))

for x in range(0, hak):
    tahmin = int(input("Tahmininizi yazınız: "))
    if tahmin < sayı:
        print("Daha fazla: ")
    elif tahmin > sayı:
        print("daha düşük: ")
    else:
        print("BAŞARDINIZ")
        break
