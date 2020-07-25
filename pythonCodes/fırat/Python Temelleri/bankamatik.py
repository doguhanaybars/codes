
SadıkHesap = {
    "ad": "Sadık Turan",
    "hesapNo": "123456789",
    "bakiye": 3000,
    "ekHesap": 2000
}

AliHesap = {
    "ad": "Ali Turan",
    "hesapNo": "1235348456789",
    "bakiye": 2000,
    "ekHesap": 1000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanımı = input("ek hesap kullanılsın mı?(e/h)")

            if(ekHesapKullanımı == "e"):
                print("paranızı alabilirsiniz")
            else:
                print(
                    f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("bakiyeniz yetersizdir.")


paraCek(SadıkHesap, 3000)
paraCek(SadıkHesap, 3000)
