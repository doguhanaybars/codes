x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

num1 = int(input("ilk sayıyı giriniz: "))
num2 = int(input("ikinci sayıyı giriniz: "))
result = num1 * num2

print(f"çarpım ile {x} sayısı arasındaki fark = {result - (x+y+z)}")


print(f"y nn x e kalansız bölümü = {y//x}")

print(f"xyz toplamının mod 3 ü = {(x+y+z) %3}")

print(f"y nin x kuvveti = {y**x}")

x, *y, z = numbers
print(f"z nin kübü = {z**3}")
print(f"y nin değerler toplamı = {y[0] + y[1] + y[2]}")
