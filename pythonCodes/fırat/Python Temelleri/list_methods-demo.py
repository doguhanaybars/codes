names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
result = names

names.insert(0, "Sena")
names.remove("Deniz")

result = "Ali" in names

names.reverse()
names.sort()
years.sort()

print(years)

markalar = []

marka = input("marka: ")
markalar.append(marka)
print(markalar)
