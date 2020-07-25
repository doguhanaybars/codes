from functools import reduce
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
your_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0
    # aynı zamanda if kullanmamayı da öğrenmiş olduk, sadece tek olduğu zaman bu def bir sayı return edecektir.


print(list(map(lambda item: item * 2, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))
print(list(zip(my_list, your_list)))

print(my_list)
