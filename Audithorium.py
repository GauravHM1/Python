print("Auditorium")
Audi=[]
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
s = int(input("Enter the number of seats: "))



for i in range(n):
    row = []  
    for j in range(m): 
        print("Enter the seat in in row",(i),"and column",(j))
        number = input()
        row.append(number)
    Audi.append(row)  

print("Matrix is:")
for row in Audi:
    print(row)