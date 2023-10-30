mark = float(input("Enter the exam mark:")) 

if mark < 0 or mark > 100:
    print('Invalied mark,Try again')
elif mark >= 70:
    print('Exceptional result!')
elif mark >= 40:
    print('Satisfactory result!')
else:
    print('You have failed.')