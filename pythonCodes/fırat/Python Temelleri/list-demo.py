car = ["Bmw", "Mercedes", "Opel", "Mazda"]
# result = len(car)
result = car[len(car) - 1]
car[-1] = "Toyota"
result = car
result = "Mercedes" in car
result = car[-2]
result = car[:3]
car[-2:] = ["Toyota", "Renault"]
result = car
result = car + ["Audi", "Nissan"]
del car[-1]
result = car
result = car[::-1]

studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 2010, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]
result = f"{studentA[0]} {studentA[1]} {2020 - studentA[2] } yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/len(studentA[3])}"

print(result)
