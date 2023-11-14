# Exercise: Using if Elif and else
# Create a Menu program that allows user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice

subjects = ["Mathematics","English","Science"]

print("Welcome back school!")
print("We provide these subjects:")
print(f"1. {subjects[0]}")
print(f"2. {subjects[1]}")
print(f"3. {subjects[2]}")

choice = int(input("Choose the number for the subject you want to learn: "))

if choice == 1:
  print(f"{subjects[choice-1]} is an excellent choice!")
elif choice == 2:
  print(f"{subjects[choice-1]} is not the greatest choice :/")
elif choice == 3:
  print(f"{subjects[choice-1]} is a very good choice!")
else:
  print("Your input doesn't seem to be correct. Please try again.")