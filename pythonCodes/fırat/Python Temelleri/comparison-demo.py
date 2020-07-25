vize1 = int(input("ilk vizeyi giriniz : "))
vize2 = int(input("ikinci vizeyi giriniz : "))
final = int(input("final giriniz : "))

ortalama = (vize1 * (6/10)) + (vize2 * (6/10)) + (final * (4/10))

if ortalama >= 50:
    print("geçti")
else:
    print("kaldı")
