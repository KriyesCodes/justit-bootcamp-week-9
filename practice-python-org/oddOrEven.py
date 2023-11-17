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


num = int(input("Enter your number: "))

evenOddOrFour(num)