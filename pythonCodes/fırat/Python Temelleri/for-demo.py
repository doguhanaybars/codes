# soru 1
sayılar = [1, 3, 5, 7, 9, 12, 19, 21]

# for x in sayılar:
#     if x % 3 == 0:
#         print(f"{x} sayısı 3 ün katıdır")

# soru 2
# toplam = 0
# for x in sayılar:
#     toplam += x
# print(toplam)

# soru 3

# for sayı in sayılar:
#     if(sayı % 2 != 0):
#         print(f"{sayı} 'nın karesi = {sayı**2}")

# soru 4
# sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# for x in sehirler:
#     if (len(x) <= 5):
#         print(x)

# soru 5

urunler = [
    {"name": "samsung S6", "price": "3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"},
]
# toplam = 0

# for urun in urunler:
#     fiyat = int(urun["price"])
#     toplam += fiyat
# print(toplam)

# soru 5
for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"])
