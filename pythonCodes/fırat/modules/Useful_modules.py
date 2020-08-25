from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 4, 5, 6, 7, 2, 6, 8, 6, 2, 1, 4, 5, 6, 2, 1, ]
# sentence = "blah blah blah thinking about python"
# print(Counter(li))
# print(Counter(sentence))

# dictionary = defaultdict(lambda: "does not exist", {"a": 1, "b": 2})

# print(dictionary["c"])

d = OrderedDict()
d["a"] = 1
d["b"] = 2

d2 = OrderedDict()
d["b"] = 2
d["a"] = 1

print(d2 == d)
# sadece içerikleri değil orderına göre de sıralar.
