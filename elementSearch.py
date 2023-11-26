def listContainsNumber(sortedList, num):
  for el in sortedList:
    if el == num:
      return True
  return False

sortedList1 = [1, 4, 7, 10, 21, 50, 55, 58, 60, 61, 79, 110, 150, 500]

print(listContainsNumber(sortedList1, 500))

