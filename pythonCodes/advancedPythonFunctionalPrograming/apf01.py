# map, filter, zip and reduce

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list
# print(multiply_by2([1,2,3]))

from functools import reduce

my_list = [1,2,3]
your_list = [10,20,30]
their_list =[5,4,3]
only_list = [1,2,3,4,5]
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumalator(acc,item):
    print(acc,item)
    return acc + item


print("first list: ",my_list)
print("Second list: ",your_list)
print("Third list: ",their_list)
print("Only list: ",only_list)

# map
print("map:",list(map(multiply_by2, my_list)))

#filter
print("filter:",list(filter(only_odd, my_list)))

#zip
print("zip:",list(zip(my_list, your_list, their_list)))

#reduce
print("--reduce--")
print("reduce: ",reduce(accumalator,only_list,0))