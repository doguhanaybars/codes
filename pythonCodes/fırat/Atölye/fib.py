fib = [1]
cift = []
count = 0


def evenfib(num):
    adding = 1
    fib.append(adding)
    for tekrar in range(0, num):
        adding = adding + fib[tekrar]
        fib.append(adding)


evenfib(31)

print(fib)


def ciftmi(fib):
    for ciftsay in range(0, len(fib)):
        if fib[ciftsay] % 2 == 0:
            cift.append(fib[ciftsay])

# deneme


ciftmi(fib)

print(cift)

for z in range(0, len(cift)):
    count = count + cift[z]

print(count)
