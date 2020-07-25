pnumbers = []


# def bolen(num):
#     for tum_bolenler in range(1, num):
#         if num % tum_bolenler == 0:
#             pnumbers.append(tum_bolenler)


# bolen(13195)


# def prime(pnumbers):
#     for x in range(2, len(pnumbers)-1):
#         # print(pnumbers[x])
#         for y in range(0, x-1):
#             if(pnumbers[x] % pnumbers[y] == 0):
#                 pnumbers.remove(pnumbers[x])


# prime(pnumbers)

# print(pnumbers)
x = 2


def prime(num):
    if num % x == 0:
        bolunmeyen = num/x
        if bolunmeyen % 2 == 0:
