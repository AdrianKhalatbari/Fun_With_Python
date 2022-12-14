# Python Program to Add Two Matrices
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]
print("Sum of 2 matrices")
for r in result:
    print(r)
print('---------------------')

# Python Program to Multiply Two Matrices
# In the multiplication of two matrices,
# the row elements of the first matrix are multiplied to the column elements of the second matrix.
a = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9]]

b = [[3, 2, 4],
     [4, 3, 6],
     [2, 7, 5]]

multiResult = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
for m in range(len(a)):
    for n in range(len(b)):
        for o in range(len(b)):
            multiResult[m][n] += a[m][o] * b[o][n]
print("Multiply of 2 matrices")
for r in multiResult:
    print(r)
print('---------------------')

# Python Program to Transpose a Matrix
F = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9],
     [8, 1, 3]]
transposeResult = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

for a in range(len(F)):
    for b in range(len(F[0])):
        transposeResult[b][a] = F[a][b]
print("Transpose of 2 matrices")
for r in transposeResult:
    print(r)
print('---------------------')
