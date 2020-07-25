cumle = input("bir cümle yazınız")

kelimeler = cumle.split()

kelimeler.sort()
print(kelimeler)

for kelime in kelimeler:
    print(kelime)
