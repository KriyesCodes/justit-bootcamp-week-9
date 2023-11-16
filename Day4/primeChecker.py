def checkPrime(num):
  if (num < 0):
    return False
  if (num <= 3):
    return True

  for i in range(2, num):
    if (num % i) == 0:
      return False
    
  return True


for i in range(31):
  if checkPrime(i):
    print(f"{i} is prime")
  else:
    print(f"{i} is not prime")