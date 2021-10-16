# new tuple
# newTuple = ('a', 'b', 'c', 'd', 'e', 'f')
# newTuple2 = tuple('abcdefghijklmnopqrstuvwxyz')
# print(newTuple)
# print(newTuple2)

# newTuple = ('a', 'b', 'c', 'd', 'e', 'g')

# accessing element via []
# print(newTuple[-1])

# from one index till another
# print(newTuple[0:4])

#Traverse through a tuple
#return the elements
# for i in newTuple:
#     print(i)

#Traverse through a tuple with range and len function
# return o index counts of any given tuple
# for i in range(len(newTuple)):
#     print(i)

# searching an element from a tuple
# returns True or False as a result
# print('a' in newTuple)

# Linear search
# def searchTup(nTup, element):
#     for i in nTup:
#         if i == element:
#             return nTup.index(i)
#     return 'The element does not exists in the Tuple'

# print(searchTup(newTuple, 'h'))

# newTuple = ('a', 'b', 'c', 'd', 'e', 'g')
# newTuple1 = (1, 2, 3, 4, 5, 6)

# tuple concatenation
# print(newTuple + newTuple1)

# * to create multiple element from one single tuple
# print(newTuple * 4)

# print(len(newTuple))
# print(max(newTuple1))
# print(min(newTuple1))

# turning list into tuple
# print(tuple([1,2,3,4,5]))

list = [0,1,2,3,4,5,6,7,8,9]

# insert an element
# list[1] = 3

# delete and element
del list[0]

print(list)