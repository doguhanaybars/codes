# def square(num):
#     return num ** 2

# numbers = [1,2,3,4,5,10]

# result = list(map(square,numbers))

# for item in result:
#     print(item)

numbers = [1,2,3,4,5,10]

result = list(map(lambda numbers: numbers ** 2,numbers))
print(result)