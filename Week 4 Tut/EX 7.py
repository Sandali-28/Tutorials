import random

double_num=0

for i in range(100):
    num1= random.randint(1,6)
    num2= random.randint(1,6)

    if num1==num2:
        double_num +=1

print(f'Out of 100 rolls, you rolled {double_num} doubles.')