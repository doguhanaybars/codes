my_list = [char for char in "hello"]
my_list2 = [num ** 2 for num in range(0, 100)]


def odd_ones(li):
    return li % 2 != 0


my_list4 = list(filter(odd_ones, my_list2))

# ya da
my_list5 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# for item in "hello":
#     my_list.append(item)

print(my_list5)
