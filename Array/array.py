# from array import *

# arr1 = array('i', [1,2,3,4,5,6])
# arr2 = array('d', [1.3,1.5,1.6])

# print(arr2)

# insertion rule
# select the index and then the element and separate it with ,
# inserting at the end of the array
# arr1.insert(6, 7)
# arr1.insert(6, 120)
# print(arr1)

# inserting in the beginning
# arr1.insert(0,0)
# print(arr1)

# Array traversal
# def traverseArray(arr):
#     for i in arr: #--- O(n)
#         print(i) #-----O(n)

# traverseArray(arr1)

# accessing array element
# def accessElement(array, index):
#     if index > len(array):
#         print('There is not element in this array')
#     else:
#         print(array[index])

# accessElement(arr1, 5)

# search/find an element in array
# from array import *
# arr1 = array('i', [1,2,3,4,5,6])

# def searchInArray(array, value):
#     for i in array:
#         if i == value:
#             return array.index(value)
#     return "The element does not exists in the array"
# print(searchInArray(arr1, 7))

# remove an element from an array
# from array import *
# arr1 = array('i', [1,2,3,4,5,6])

# arr1.remove(4)
# print(arr1)


# from array import *

# 1. Create an array
# my_array = array('i', [1,2,3,4,5,6,7,8,9,10])

# in the above mentioned array the i represent the integer

# 2. traversing through array
# print("step 1")
# for i in my_array:
#     print(i)

# 3. Access individual elements through indexes
# print("step 2")
# print(my_array[0])

# 4. Append any value to an array with append() method
# my_array.append(11)
# print("step 3")
# print(my_array)

# 5. Insert value in an array with insert() method
# my_array.insert(10, 11)
# print("step 4")
# print(my_array)

# 6. Extend python array using extend method()
# my_array1 = array('i', [11,12,13,14])
# my_array.extend(my_array1)
# print("step 5")
# print(my_array)

# 7. Add items from list into array using fromlist() method
# temList = [20,21,23,24,25]
# my_array.fromlist(temList)
# print("step 6")
# print(my_array)

# 8. Remove any array element using remove() method
# only delete the first element it finds in the array 
# my_array.remove(21)
# print("step 7")
# print(my_array)

# 9. remove last element using pop() method
# my_array.pop(1)
# print("step 8")
# print(my_array)

# 10. Fetch any element through its index using index() method
# print("step 9")
# print(my_array.index(5))

# 11. Reverse a python array using reverse() method
# print("step 10")
# my_array.reverse()
# print(my_array)

# 12. Get array buffer information through buffer_info() method
# print("step 11")
# print(my_array.buffer_info())

# 13. Check for number of occurrences of an element using count() method
# print("step 12")
# my_array.append(12)
# print(my_array.count(11))
# print(my_array)

# 14. Converting array to string loop
# from array import *
# my_array = array('i', [1,2,3,4,5,6,7,8,9,10])

# print("step 12")
# my_array.append(12)
# print(my_array.count(11))
# print(my_array)

# print("step 13")
# strTemp = ''
# for i in my_array:
#     strTemp += str(i)
# print(strTemp)

# 15. Convert array to a python list with same elements using tolist() method
# print("step 14")
# print(my_array.tolist())

# 16. Append a string to char array using fromstring() method
# print("step 15")

# 17. array slicing
# print("step 16")
# print(my_array[0:4])

# Two dimensional array
# Day 1 - 11, 15, 16, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np
twoDArray = np.array([[11, 15, 16, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# insertion in two dimensional array
# newTwoDArray = np.insert(twoArray, 0, [1,2,3,4], axis=0)
# print(newTwoDArray)

# insertion using append method
# newTwoDArray = np.append(twoArray, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

# access an element of two dimensional array
# def accessElement(array, rowIndex, colIndex):
#     if rowIndex >= len(array) or colIndex >= len(array[0]):
#         print("Incorrect Index")
#     else:
#         print(array[rowIndex][colIndex])
# accessElement(twoDArray,2,2)

# Traversing a two diemnsional array
# def traverseTDArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])

# traverseTDArray(twoDArray)

# searching for an element in  two dimensional array
# def searchTDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return "The value is located at index "+str(i)+" "+str(j)
#     return "The element is not found"

# print(searchTDArray(twoDArray, 9))

# deletion of an element from two dimensional array
newTDArray = np.delete(twoDArray, 2, axis=0)
print(newTDArray)