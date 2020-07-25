# key - value

# dict olmadan list ile nasıl yapılır

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")])

# ----------------------------------------------------------

# plakalar = {
#     "kocaeli": 41,
#     "istanbul": 34
# }
# plakalar["ankara"] = 6

# print(plakalar)

# ------------------------------------------------------------

users = {
    "sadıkturan": {
        "age": 36,
        "mail": "sadik@gmail.com",
        "adres": "asfişkhjdnşfk",
        "telefon": "12345486947"
    },
    "cınarturan": {
        "age": 2,
        "mail": "cınar@gmail.com",
        "adres": "gfdshdthd",
        "telefon": "657489321"
    }
}

print(users["cınarturan"]["age"])
