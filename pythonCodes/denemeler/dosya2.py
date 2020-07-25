# try:
#     file = open("newfile.txt","r",encoding=("utf-8"))
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("Dosya Kapandı")
#     file.close()

file = open("newfile.txt","r",encoding=("utf-8"))

#for döngüsü

# for i in file:
#     print(i, end="")

#read() fonksiyonu

# content1 = file.read()
# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding=("utf-8"))

# content2 = file.read()
# print("içerik 2")
# print(content2)


# content = file.read(5)
# print(content)

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

liste= file.readlines()
print(liste[0])
print(liste[1])
print(liste[3])
print(liste)


file.close()