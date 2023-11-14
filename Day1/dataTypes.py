# myList = [2,"two", 2.5, True]
# print(type(myList))
# print(myList)

# myTuple = (2, "two", 2.5, True)
# print(type(myTuple))
# print(myTuple)

# mySet = {2, 2, 2, 2, "test", 5, "test", 1.3, 1.30}
# # duplicates are removed, not indexed
# print(type(mySet))
# print(mySet)



myDictionary = {0:{"firstName":"Kriyes",
                   "lastName":"Mahendra",
                   "occupation":"student"},
                1:{"firstName":"John",
                   "lastName":"Doe",
                   "occupation":"architect"}}

print(f"First Name: {myDictionary[0]['firstName']}\nOccupation: {myDictionary[0]['occupation']}")
print(f"First Name: {myDictionary[1]['firstName']}\nOccupation: {myDictionary[1]['occupation']}")