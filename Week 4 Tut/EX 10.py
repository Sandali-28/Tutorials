import random
hidden_num = random.randint(1, 20)
try:
    count = 0
    max_count = 5

    while count < max_count:
        guess = int(input("Guess the number between 1 and 20: "))
        count += 1
    
        if guess == hidden_num:
            print("Congratulations! You guessed the correct number", hidden_num, "in", count, "attempts.")
            break
        elif guess < hidden_num:
            print(guess, "is too low,try again.")
        else:
                print(guess,"is too high,try again.")

    if count == max_count:
        print("Sorry, you've run out of guesses. The hidden number was", hidden_num, ".")

except ValueError:
    print('Please enter a valid integer.')