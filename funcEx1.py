def userName4(fullName, address, interest):
  return print(f"my name is {fullName}, my address is {address} and my interest is {interest}")

fullName = str(input("Enter your full name: ")) or "Kriyes Mahendra"
address = str(input("Enter your address: ")) or "London"
interest = str(input("Enter your interest: ")) or "NOT leetcode"

print(userName4(fullName, address, interest))