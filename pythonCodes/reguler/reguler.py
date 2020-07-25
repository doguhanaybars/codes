import re

pattern = re.compile('this')
string = 'search this inside of this text please!'


print('search' in string)

a = re.search('this',string)
print(a.span())

b = pattern.search(string)
print(b.group())

c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)
print(d)