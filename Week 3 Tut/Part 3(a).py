print("If you want to convert from Celsius to Fahrenheit enter 1")
print("If you want to convert from Fahrenheit to Celsius enter 2")

num = int(input("Enter the number"))

temperature = float(input("Enter a temperature in the correct unit"))

fahrenheit = ((temperature * 1.8)+32)

celsius = ((temperature - 32)/1.8)

if num == 1:
    print("Fahrenheit", fahrenheit)
elif num == 2:
    print("Celsius", celsius)
else:
    print("Invalid option entered")
