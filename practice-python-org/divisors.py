def getDivisors(dividend):
  divisors = [1]

  for i in range(2, (dividend//2)+1):
    if dividend % i == 0:
      divisors.append(i)
  
  divisors.append(dividend)
  return divisors


dividend = int(input("Enter number you want the divisors of: "))

print(getDivisors(dividend))