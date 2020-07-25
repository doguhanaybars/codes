sayı = int(input("bir sayı giriniz : "))
x = 1
asalmı = True
if sayı == 1:
    print("1sayısı asal değildir.")

for i in range(2, sayı):
    if(sayı % i == 0):
        asalmı = False

if asalmı == True:
    print("Sayınız asaldır")
else:
    print("Sayınız asaldeğildir")
