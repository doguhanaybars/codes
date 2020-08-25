# all generators is iterable but not all iterables are not generators

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result
# my_list = make_list(100)
# print(my_list)

def generator_(num):
    for i in range(num):
        yield i*2


# for item in generator_():
#     print(item)
# buradaki fark range in yarattığı tüm sayıları bellekte tutmak yerine zamanı geldiğinde ortaya çıkartarak daha rahat bir çözüm sağlatmak


g = generator_(1000)
next(g)
next(g)
print(next(g))
