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

# print("Welcome to the table quiz.\n")
# num = int(input("Enter a number: "))

# if (num <= 0):
#   print("Please enter a positive number")
# else:
#   for i in range(1, num+1):
#     answer = int(input(f" What is {i} x {num}? "))
#     correct = i * num
#     if answer == correct:
#       outcome = "Correct"
#     else:
#       outcome = "Incorrect"
#     print(f"{outcome}, the answer is {correct}")

# print("Program End")

# Task 4

# Print out a multiplication table of your choice

num = int(input("Enter number for multiplication: "))

for i in range(1, num+1):
  print(f"{i} x {num} = {i * num}")