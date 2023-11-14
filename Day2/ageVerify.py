# Task:
# Create an age verification system that checks a users age for restricted products being purchased.
# Include a nested if else statement for the verification process.

items = {
  1: {"name":"chocolate", "ageRequired":7},
  2: {"name":"alcohol", "ageRequired":18},
  3: {"name":"cigarettes", "ageRequired":18},
  4: {"name":"toy", "ageRequired":11},
  5: {"name":"apple", "ageRequired":3}
}

print("Welcome to the shop!")
print("We have these items available:")
print(f"1. {items[1]['name']}")
print(f"2. {items[2]['name']}")
print(f"3. {items[3]['name']}")
print(f"4. {items[4]['name']}")
print(f"5. {items[5]['name']}")

choice = int(input("Enter the item number of the item you wish to buy: "))
age = int(input("Enter your age: "))

if choice in items:
  if age <= 0:
    print("Your age cannot be zero or negative")
  else:
    if (age >= items[choice]["ageRequired"]):
      print(f"You have bought {items[choice]['name']}")
    else:
      print(f"You are not old enough to buy {items[choice]['name']}")
else:
  print("Your item choice is invalid")

