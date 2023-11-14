num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
smallerNum = 0

if num1 <= num2:
  smallerNum = num1
else:
  smallerNum = num2

print(f"The smaller number is {smallerNum}")