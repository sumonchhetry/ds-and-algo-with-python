# Creating various lists
# integers = [1,2,3,4]
# print(integers)

# stringList = ["Rice", "Potato", "Oil", "Bread"]
# print(stringList)

# mixedList = [1, 2.6, "Hello"]
# print(mixedList)

# nestedList = [1,4,5, [1.6, 1.68], ['test list']]
# print(nestedList)

# empty = []
# print(empty)

# Accessing/Traversing List
# shoppingList = ["Milk", "Cheese", "Butter"]
# print(shoppingList[1])
# checking if the element exists in the list or not with in operator
# print("Milk" in shoppingList)
# if we put (-) value to access a list it will starts from the last element in the list 
# print(shoppingList[-1])

# for i in shoppingList:
#     print(i)

# another approach. this way we 
# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i]+"+"
#     print(shoppingList[i])

# Update/Insert in a list
# myList = [1,2,3,4,5,6,7,8]
# print(myList)
# [] operator use the index and the value gets assigned in that index inside the list
# myList[2] = 33
# myList[4] = 1652
# print(myList)

# insert() method
# myList.insert(0, 159)
# print(myList)

# append() method
# myList.append(6005)
# print(myList)

# expend() method
# newList = [11,12,15,16]
# myList.extend(newList)
# print(myList)

# Slicing a list
# myList = [1,2,3,4,5,6,7,8]
# myList[0:2] = ['x','y']
# print(myList[:])

# pop() method also used for deleting an item from the list they are 0 based 
# myList.pop(2)
# print(myList)

# del method
# myList = [1,2,3,4,5,6,7,8]
# del myList[0]
# print(myList)

# remove() method is very useful when you know the element
# myList.remove(8)

# print(myList)

# Searching for an element in the list
# myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 9000]

# in operator
# if 1100 in myList:
#     print(myList.index(20))
# else:
#     print("the value does not exists in the list")

# linear search
# def searchList(list, value):
#     for i in list:
#         if i == value:
#             return list.index(value)
#     return "The value does not exists in the list"

# print(searchList(myList, 10))

# List operations / functions
# a = [1,2,3]
# b = [4,5,6]

# + operator to do list concatonate or joining them together and make a single list
# c = a + b
# print(a+b)

# * operator 
# a = [0,1,2,3,4,5]

# the second value multiply the list and make clone of the elements
# a = a * 4
# print(a)

# len method returns the count of the list
# a = [0,1,2,3,4,5]
# print(len(a))

# max method is to return the higgest value in the list
# a = [0,1,2,3,4,5]
# print(max(a))

# min method is to return the lowest value in the list
# a = [0,1,2,3,4,5]
# print(min(a))

# sum method is to return the sum of all items in the list
# a = [0,1,2,3,4,5]
# print(sum(a))

# finding the average of a list
# a = [0,1,2,3,4,5]
# print(sum(a) / len(a))

# code challenge
# myList = []

# Strings and Lists
# converting strings to list
# a = 'span span spam'
# b = list(a)
# print(b)

# spliting a string into a list
# a = 'span-span-spam'
# delimiter = '-'
# b = a.split(delimiter)
# print(b)

# join function to convert a list to a string
# a = 'span-snap-spam'
# by using delimiter we are removing the common character
# delimiter = '-'
# b = a.split(delimiter)
# print(b)
# print(delimiter.join(b))

# Array vs List
# import numpy as np

# myArray = np.array([1,2,3,4,5,6])
# myList = [1,2,3,4,5,6,7,8]

# print(myArray/2)