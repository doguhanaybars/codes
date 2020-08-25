import re

pattern = re.compile(r"[A-Za-z0-9!'^]{8,}\d")

pswd = input("şifrenizi giriniz : ")

a = pattern.search(pswd)

print(a)
