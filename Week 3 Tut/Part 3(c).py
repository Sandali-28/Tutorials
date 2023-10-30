cost = float(input("Enter the cost of meal: Rs"))
num = int(input("Enter your satisfaction level using rating(1 = Totally Satisfied,2 = Satisfied,3 = Dissatisfied)"))

if num == 1:
    tip = cost * 0.2
    print("Satisfaction level",num)
elif num == 2 :
    tip = cost * 0.15
    print("Satisfaction level",num)
elif num == 3 :
    tip = cost * 0.1
    print("Satisfaction level",num)
else:
    print ("Invalied satisfication level")
    tip = 0

print("Tip: Rs",tip)