import re

pattern = re.compile("this")
string = "search this inside of this text please!"

# print("search" in string)

# a = re.search("this", string)
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
# print(a.start())
print(a.group())
print(d)
