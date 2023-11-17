a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def commonBetweenLists(list1, list2):
  if (len(list1) < len(list2)):
    smallerList = list1
    largerList = list2
  else:
    smallerList = list2
    largerList = list1
  
  newList = []
  for i in smallerList:
    if i in largerList:
      newList.append(i)

  return newList

