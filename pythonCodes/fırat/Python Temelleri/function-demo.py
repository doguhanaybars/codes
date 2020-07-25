# # 1
# name = input("Bir isim giriniz: ")
# time = int(input("tekrar sayısınız giriniz: "))


# def tekrar(name, time):
#     for x in range(0, time):
#         print(f"{x+1}. {name}")

# ya da
# def yazdır(kelime, adet):
#     print(kelime * adet)

# tekrar(name, time)


# 2

# def listeyeCevir(*args):
#     list = []

#     for param in args:
#         list.append(param)
#     return list


# print(listeyeCevir(1, 2, 3, 4, 5, 89, 564, "asdw"))

# 3

# def asal(num1, num2):
#     for x in range(num1, num2+1):
#         if x > 1:
#             for i in range(2, x):
#                 if (x % i == 0):
#                     break
#             else:
#                 print(x)


# print(asal(10, 100))

# 4
sayı = int(input("bir sayı giriniz : "))


def tambolen(num1):
    tambolenler = []
    for i in range(2, num1):
        if(num1 % i == 0):
            tambolenler.append(i)

    return tambolenler


print(tambolen(sayı))
