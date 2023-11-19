def fib(fibList, size):
  if size == 0:
    return fibList
  fibList.append(fibList[-1] + fibList[-2])
  size -= 1
  return fib(fibList, size)

def generateFibonacciList(size):
  if size <= 0:
    return []
  if size == 1:
    return [1]
  if size == 2:
    return [1, 1]
  if size > 1000:
    return "This is beyond the recursion limit"
  
  size -= 3;
  fibList = [1, 1, 2]

  return fib(fibList, size)

amount = int(input("Enter quantity of fibonnaci numbers to generate: "))
print(generateFibonacciList(amount))