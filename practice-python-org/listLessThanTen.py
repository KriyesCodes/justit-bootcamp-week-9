a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def lessThan5():
  for i in a:
    if i < 5:
      print(f"{i} is less than 5")

def listLessThan5():
  newList = []
  for i in a:
    if i < 5:
      newList.append(i)
  print(newList)

def oneLineListLessThan5():
  print([i for i in a if i < 5])

oneLineListLessThan5()