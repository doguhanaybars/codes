# def square(num): return num ** 3


# numbers = [1, 3, 5, 9]

# result = list(map(lambda num: num ** 2, numbers))

# for item in map(square, numbers):
#     print(item)


# def result(num): return num ** 2


# print(result)

numbers = [1, 3, 5, 9, 10, 4]


# def check_even(num): return num % 2 == 0
# def check_even(num): return num % 2 == 0

def check_even(num): return num % 2 == 0

# result = list(filter(lambda num: num % 2 == 0, numbers))


result = list(filter(check_even, numbers))

print(result)
