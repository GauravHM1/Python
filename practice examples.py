#check if the number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num,"is Even")
else:
    print(num,"is Odd")

#Find the greatest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a>=b) and (a>=c):
    greatest = a
elif (b>=a) and (b>=c):
    greatest = b
else:
    greatest = c

print("The greatest number is:",greatest)

#Simple calculator using if-else
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")