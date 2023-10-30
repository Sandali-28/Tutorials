total = 0   # sum of scores
count = 0   # number of scores entered

# get one score and convert string to integer 
score = int(input("Enter score, (Enter -9 to end): "))

# while loop
while score != -9:
  total += score
  count += 1
  score = int(input("Enter a score: "))

# print average of scores entered
average = total / count
print("The average score is:", average)