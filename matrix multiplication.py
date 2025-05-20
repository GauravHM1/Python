n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix1 = []
matrix2 = []
result = []

for i in range(n):
    row = []  
    for j in range(m): 
        number = int(input("Enter the number for matrix 1: "))
        row.append(number)
    matrix1.append(row)  

for i in range(n):
    row2 = []  
    for j in range(m): 
        number = int(input("Enter the number for matrix 2: "))
        row2.append(number)
    matrix2.append(row2)  

print("Matrix is:")
for row2 in matrix1:
    print(row2)

print("Matrix is:")
for row in matrix2:
    print(row)

for i in range(n):
    row0=[]
    for j in range(m):
        row0.append(0)
    result.append(row0)

for i in range(n):
    for j in range(m):
        for k in range(m):
            result[i][j] += matrix1[i][k] * matrix2[k][j]


print("results is:")
for row in result:
    print(row)
