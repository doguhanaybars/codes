count = 0
for sayı in range(0, 1000):
    if sayı % 3 == 0 or sayı % 5 == 0:
        count = count+sayı

print(count)
