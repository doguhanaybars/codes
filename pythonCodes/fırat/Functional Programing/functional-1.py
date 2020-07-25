from functools import reduce

my_pets = ["sisi", "bibi", "titi", "carla"]


def capit(li):
    return li.upper()


print(list(map(capit, my_pets)))

my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

scores = [73, 20, 65, 19, 76, 100, 88]


def half(li):
    return li > 50


print(list(filter(half, scores)))
