lis1 = [1, 3, 2, 4]
lis2 = [5, 2, 1, 0]
res = []

for index in range(0,len(lis1)):
    res.append(lis1[index] + lis2[index])
print(res)