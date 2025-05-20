n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []

for i in range(n):
    row = []  
    for j in range(m): 
        number = int(input("Enter the number: "))
        row.append(number)
    matrix.append(row)  

print("Matrix is:")
for row in matrix:
    print(row)