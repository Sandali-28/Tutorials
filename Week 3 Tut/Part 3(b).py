num1 = int(input("Enter the first integer"))
op = input("Enter the  the operator")
num2 = int(input("Enter the second integer"))

if op == '+':
    total = num1 + num2
    print(total)
elif op == '-':
    total = num1 - num2
    print(total)
elif op == '*':
    total = num1 * num2
    print(total)
elif op == "/":
    if num2 == 0:
        print("Error")
    else:
        total = num1 / num2
        print(total)
else:
    print("Invalid Operator")
