x = [[2,4],
     [3,5]]
y = [[4,2],
     [5,3]]
result = [[0,0],
          [0,0]]
#iterate through rows of x
for i in range(len(x)):
    #iterate through columns of y
    for j in range (len(y[0])):
        #iterate through rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for r in result:
    print(r)