def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(multiply_by2([1, 2, 3]))
print(multiply_by2(list))
