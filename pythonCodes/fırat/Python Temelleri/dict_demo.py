ogrenciler = {}

ogrenci_numarası = input("lütfen öğrenci numarası giriniz: ")
name = input("ogrenci adı:")
surname = input("ogrenci soyad:")
phone = input("ogrenci telefon:")

# ogrenciler[ogrenci_numarası] = {
#     "ad": name,
#     "soyad": surname,
#     "telefon": phone
# }
ogrenciler.update({
    ogrenci_numarası: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})


print(ogrenciler)
