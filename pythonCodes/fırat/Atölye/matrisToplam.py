x = [[1, 3, 5], [2, 4, 1], [1, 5, 7]]

y = [[3, 3, 4], [2, 4, 1], [3, 5, 4]]

sonuc = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for a in range(3):
    for b in range(3):
        sonuc[a][b] = x[a][b] + y[a][b]

print(sonuc)
