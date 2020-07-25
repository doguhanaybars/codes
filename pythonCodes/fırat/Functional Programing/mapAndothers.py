my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
your_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0
    # aynı zamanda if kullanmamayı da öğrenmiş olduk, sadece tek olduğu zaman bu def bir sayı return edecektir.


# print(list(filter(only_odd, my_list))) #diğerinde olduğu gibi asıl veriye dokunulmadı tek olanlar incelenip filter için kullanılan listeye atılmış oldu.

# print(list(map(multiply_by2, my_list)))
# map, functional programing için gerekli olan şeye sahiptir. dışarıdaki dünyaya karışmamak. listeden değeri alıp istenilen fonksiyonu gerçekleştirir ancak asıl
# veriye dokunmaz
print(list(zip(my_list, your_list)))

print(my_list)
