def removeDuplicatesSet(lst):
  return set(lst)

lst = [1, 2, 3, 3, 5, 10, "ten", "ten", False, False, True]

def removeDuplicatesLoop(lst):
  newList = []

  for i in range(len(lst)):
    if lst[i] not in newList:
      newList.append(lst[i])
  
  return newList

print(removeDuplicatesSet(lst))
print(removeDuplicatesLoop(lst))