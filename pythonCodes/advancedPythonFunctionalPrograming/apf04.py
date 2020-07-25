#squre
my_list = [5,4,3]

print(list(map(lambda num: num**2,my_list)))

#List Sorting

a = [(0,20),(4,3),(10,-1),(9,9)]

a.sort(key=lambda x: x[1])
print(a)