import random

# Generate a random number between 0 and 1.
coin_flip = random.randint(0, 1)

# Print "Heads" if the random number is 0, otherwise print "Tails".
if coin_flip == 0:
  print("Heads")
else:
  print("Tails")
