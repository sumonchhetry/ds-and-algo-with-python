# numDays = int(input("How many day's of temperature ? "))
# total = 0
# temp = []
# for i in range(numDays):
#     nextDay = int(input("Day " + str(i+1) + "'s high temp: "))
#     temp.append(nextDay)
#     total += temp[i]

# average = round(total/numDays,2)
# print("\nAverage = " + str(average))
# above = 0
# for i in temp:
#     if i > average:
#         above += 1
# print(str(above) + " day(s) above average.")

# missing number
# Q. How to find the missing number in the integer array of 1 to 100 ?
# the trick is n(n+1)/2
# myList = [1,2,3,4,5,6,7,9,10]

# def missingNum(list, n):
#     sum1 = round(10*11/2)
#     sum2 = sum(list)
#     print(sum1-sum2)
# missingNum(myList, 10)

# Two sum problem - Leetcode
# def findPairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i, j)
# myList = [1,2,3,4,5,6]
# findPairs(myList, 5)

# How to check if an array contains a number
# import numpy as np

# myArray = np.array([1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20])

# def findNumber(array, number):
#     for i in range(len(array)):
#         if array[i] == number:
#             print(i)

# findNumber(myArray, 1)

# How to find the maximum product of two integers in the array where all elements are positive
# import numpy as np

# myArray = np.array([15, 15, 16, 18, 23, 96, 24, 36, 36, 48])

# def findMaxProduct(array):
#     maxProduct = 0
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if array[i] * array[j] > maxProduct:
#                 maxProduct = array[i] * array[j]
#                 pairs = str(array[i]) + ',' + str(array[j])
#     print(pairs)
#     print(maxProduct)
# findMaxProduct(myArray)

# Is Unique : Implement an algorithm to determine if a list has all unique characters, using python list
# myList = [1, 16, 27, 2, 35, 26, 85, 16, 57, 25, 69, 45]

# def isUnique(list):
#     newList = []
#     for i in list:
#         if i in newList:
#             print(i)
#             return False
#         else:
#             newList.append(i)
#     return True

# print(isUnique(myList))

# Permutation
# def permutation(list1, list2):
    # check the length of both list and return false if they are not equal in length
    # if (len(list1) != len(list2)):
    #     return False
        # sort the list
    # list1.sort()
    # list2.sort()
    # if equal return true
    # if list1 == list2:
    #     return True
        # or return false
#     else:
#         return False
# list1 = ['a', 'b', 'c', 'd']
# list2 = ['a', 'c', 'e', 'd']

# print(permutation(list1,list2))

# Rotate Matrix gievn an image represented by an NxN matrix write a method to rotate the image by 90 degree
# import numpy as np

# myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(myArray)

# def rotateMatrix(matrix):
#     n = len(matrix)
#     for layer in range(n//2):
#         first = layer
#         last = n - layer -1
#         for i in range(first,last):
            # save top element
            # top = matrix[layer][i]
            # move left element to top
            # matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            # matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right element to buttom
            # matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top to right
#             matrix[i][-layer-1] = top
#     return matrix

# print(rotateMatrix(myArray))

# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6): 
#     print(arr[i], end = " ")

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
 
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
 
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
 
# print(sum)

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
 
#     for row in m:
#         for element in row:
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))

# write a function which takes in a string and returns the count of each character in the string

# Step - 1
charCount = ('bbbb')
charCount = ('Hello')

# step -2 Complex example
"My name is Sumon"

# step - 3 empty
charCount('')

# Step - 4 invalid input
charCount(1)

def charCount(str):
    # declare an object to return at the end
    # loop over the string
    # if the character is in out object add one to the value
    # if the character is not in out object then add that char to our object with the value of one
    # return an object
    
