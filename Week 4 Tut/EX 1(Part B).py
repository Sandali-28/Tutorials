import random
hidden_num = random.randint(1, 20)
try:
    hidden_num = 6
    guess = 0

    guess = int(input("Enter a guess number between 1 and 20: "))

    while guess != hidden_num:
        print(guess,"is not correct.Please try again.")
        guess = int(input("Enter a guess number between 1 and 20: "))

    print(guess,"is correct")

except ValueError:
    print('Please enter a valid integer.')