n = int(input("Enter the number of rows: "))
matrix = []

def diagonalsum1(matrix):
    total1 = 0
    for i in range(len(matrix)):
        total1 += matrix[i][i]
    return total1

def diagonalsum2(matrix):
    total2 = 0
    for i in range(len(matrix)):
        total2 += matrix[i][len(matrix)-1-i]
    return total2   

for i in range(n):
    row = []  
    for j in range(n): 
        number = int(input("Enter the number: "))
        row.append(number)
    matrix.append(row)  

print("Matrix is:")
for row in matrix:
    print(row)

sum1= diagonalsum1(matrix)
print("The diagonal sum 1 is: ",sum1)
sum2= diagonalsum2(matrix)
print("The diagonal sum 2 is: ",sum2)

total_sum = sum1 + sum2

if n % 2 == 1:
    center = matrix[n // 2][n // 2]
    total_sum -= center

print("The total sum is: ",total_sum)