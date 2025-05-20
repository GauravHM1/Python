a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

def add(a,b):
    print("Sum is = ",a+b)
    
def sub(a,b):
    print("Subtract is = ",b-a)

def multiply(a,b):
    print("multiply value is = ",a*b)

def divide(a,b):
    print("Divide value is = ",a/b)

if (a>b):
    add(a,b)

if (a<b):
    sub(a,b)

if (a==b):
    multiply(a,b)

if (a>=b):
    divide(a,b)


