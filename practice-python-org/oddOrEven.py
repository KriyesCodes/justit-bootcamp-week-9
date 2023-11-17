def evenOrOdd(num):
  if (num % 2 == 0):
    print("The number you input is even")
  else:
    print("The number you input is odd")

def evenOddOrFour(num):
  if (num % 2 == 0):
    if (num % 4 == 0):
      print("The number you input is a multiple of 4")
    else:
      print("The number you input is even")
  else:
    print("The number you input is odd")

def checkDivisible(dividend, divisor):
  if (dividend % divisor == 0):
    print(f"{dividend} is divisible by {divisor}")
  else:
    print(f"{dividend} is not divisible by {divisor}")

dividend = int(input("Enter the number to check: "))
divisor = int(input("Enter the divisor to check with: "))

checkDivisible(dividend, divisor)