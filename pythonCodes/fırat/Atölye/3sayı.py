sayı1 = int(input("Birinci sayıyı giriniz:"))
sayı2 = int(input("İkinci sayıyı giriniz:"))
sayı3 = int(input("Üçüncü sayıyı giriniz:"))

if sayı1 > sayı2:
    if sayı1 > sayı3:
        print("Sayı1 büyüktür")
    elif sayı3 > sayı1:
        print("sayı3 büyüktür")
else:
    if sayı2 > sayı3:
        print("sayı 2 büyüktür.")
    else:
        print("sayı 3 büyüktür.")
