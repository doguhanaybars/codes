# Soru 1

# isim = input("Lütfen isminizi giriniz: ")
# yaş = int(input("Lütfen yaşınızı giriniz :"))
# eğitim = input("lütfen eğitim durumunuzu giriniz: ")

# if yaş >= 18:
#     if (eğitim == "lise") or (eğitim == "üniversite"):
#         print("Ehliye alabilirsiniz.")
#     else:
#         print("Ehliyet almaya uygun değilsiniz.")
# else:
#     print("Ehliyet almaya yeşınız uygun değil.")

# soru 2

# yazılı1 = int(input("ilk yazılıyı giriniz : "))
# yazılı2 = int(input("ikinci yazılıyı giriniz : "))
# sozlu = int(input("sözlü notunu giriniz : "))

# toplam = (yazılı1 + yazılı2 + sozlu) / 3

# if toplam >= 0 and toplam < 25:
#     print("Genel notunuz sıfırdır")
# elif toplam >= 25 and toplam < 45:
#     print("genel notunuz birdir")
# elif toplam >= 46 and toplam < 55:
#     print("genel notunuz ikidir")
# elif toplam >= 55 and toplam < 70:
#     print("genel notunuz üçdür")
# elif toplam >= 70 and toplam < 85:
#     print("genel notunuz dörtdür")
# else:
#     print("genel notunuz beşdir")

# soru 3

from datetime import datetime
import locale

alınan_zaman = input("Arabayı aldığınız zamanı giriniz : ")
alınan_zaman = alınan_zaman.split("/")
trafiğeçıkış = datetime(int(alınan_zaman[0]), int(
    alınan_zaman[1]), int(alınan_zaman[2]))

simdi = datetime.now()

fark = simdi - trafiğeçıkış

days = fark.days
