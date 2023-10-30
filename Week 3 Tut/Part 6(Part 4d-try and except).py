num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
   operation = input("Enter the operation (+, -, *, /): ")
   if operation == "+":
    result = num1 + num2
    print("The result is:", result)
   elif operation == "-":
    result = num1 - num2
    print("The result is:", result)
   elif operation == "*":
    result = num1 * num2
    print("The result is:", result)
   elif operation == "/":
    result = num1 / num2
    print("The result is:", result)
   else:
    print("Invalid operation.")

except ZeroDivisionError:
    print("Cannot divide by zero.")