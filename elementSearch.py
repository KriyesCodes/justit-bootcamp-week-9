def listContainsNumber(sortedList, num):
  for el in sortedList:
    if el == num:
      return True
  return False

def binarySearch(sortedList, num):
  leftIndex = 0
  rightIndex = len(sortedList) - 1
  # iterations = 0;

  while True:
    midIndex = (rightIndex + leftIndex) // 2
    # iterations += 1
    # print(f"Iteration: {iterations}")
    # print(f"leftIndex: {leftIndex}")
    # print(f"rightIndex: {rightIndex}")
    # print(f"midIndex: {midIndex}")
    # print("----------------------")
    
    if midIndex < leftIndex or midIndex > rightIndex or midIndex < 0:
      return False
    
    if num == sortedList[midIndex]:
      return True
    elif num < sortedList[midIndex]:
      rightIndex = midIndex - 1
    else:
      leftIndex = midIndex + 1

    # if iterations > 10:
    #   break

sortedList1 = [1, 4, 7, 10, 21, 50, 55, 58, 60, 61, 79, 110, 150, 500]

print(listContainsNumber(sortedList1, 500))

