# name = "Tim"

# for letter in name:
#   print(letter)


# array = (5, 6, 7, 8, 9, 10)

# for i in array:
#   print(i)


# for i in range(1,7):
#   print(i)


# Task 1 Create a countdown
# for i in range(10, 0, -1):
#   print(i, "mississippi")

#-----------------------

# Task 2
# Complete the code below to iterate through both lists,
# add comment to explain your code

# highscore = [125, 63, 35, 12]
# for score in highscore:
#   #score variable stores the value at the list index
#   print(score)

# usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]

# for user in usersList:
#   #user variable stores the value at the list index
#   print(user)


#-----------------------

# Task 3
# Debug and fix the multiplication program below 
# add comment where you fix the bugs

print("Welcome to the table quiz.\n")
num = int(input("Enter a number: "))


for i in range(1, num+1):
  answer = int(input(f" What is {i} x {num}? "))    
  print(f"Your answer is {answer} ")
  correct = i * num
  if answer == correct:
    print("Correct")
  else:
    print(f"Incorrect, the answer is {correct}")

print("Finished")