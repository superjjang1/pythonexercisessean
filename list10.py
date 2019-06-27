lis1 = [[1, 3, 2],
       [4, 9, 10]]
lis2 = [[5, 2, 1],
       [0, 4, 11]]
res = [[0, 0, 0],
       [0, 0, 0]]

for i in range(len(lis1)):
    for j in range(len(lis1[0])):
        res[i][j] = (lis1[i][j] + lis2[i][j])
print(res)