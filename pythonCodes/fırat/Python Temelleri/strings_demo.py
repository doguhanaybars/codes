website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

# 1
print(f"course karakter dizisinde {len(course)} kadar karakter vardır")
# 2
print(f"www yazmak için şuradadır {website[7:10]}")

print(f"com yazmak için şuradadır {website[-3:]}")


# tersten yazdırmak için
result = course[::-1]
print(result)
