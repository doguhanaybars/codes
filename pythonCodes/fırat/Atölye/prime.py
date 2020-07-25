bolenler = []
prime = []


def bolen(num):
    for x in range(2, num):
        if(num % x == 0):
            bolenler.append(x)


bolen(13195)

print(bolenler)


def primealma(bolenler):
    for z in range(0, len(bolenler)):
        for a in range(2, z-1):
            if bolenler[z] % a == 0:
                continue
            else:
                prime.append(bolenler[z])


primealma(bolenler)
print(prime)
