sayi = int(input("bir sayı giriniz:"))

for x in range(2, sayi):
    if sayi % x == 0:
        print("sayı asal değildir")
        break
    else:
        print("sayı asaldır")
        break
