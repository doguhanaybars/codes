numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)

print(myList)

myList = [letter.capitalize() for letter in myString]
print(myList)

years = [1983, 1999, 2008, 1956, 1986]

ages = [(2020 - bdate) for bdate in years]
print(ages)

result = [x if x % 2 == 0 else "TEK" for x in range(10)]
print(result)

result = []

for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

numbers = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
