# Extension Exercise (may require some additional independent research!!):
# 1) Use if else to find item from a list
# 2) print the index value if the item is found
# 3) otherwise print a message "item not in list/not found"

fruits = ["apple", "banana", "pear", "orange", "mango"]

choice = str(input("What fruit would you like? ")).lower()

if choice in fruits:
  print("That's a fine choice!")
else:
  print("We don't have that fruit, sorry.")