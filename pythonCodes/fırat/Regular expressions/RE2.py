import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"

# print("search" in string)

# a = re.search("this", string)
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# # print(a.start())
# print(a.group())
# print(d)

a = pattern.search(string)
print(a)
