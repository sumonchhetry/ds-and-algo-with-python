#  Big O notation
# def findBiggestNUmber(sampleArray):
#     biggestNumber = sampleArray[0] #----- O(1)
#     for index in range(1, len(sampleArray)): #-----O(n)
#         if sampleArray[index] > biggestNumber: # ------ O(1)
#             biggestNumber = sampleArray[index] # ------ O(1)

#     print(biggestNumber) #----- O(1)

# measuring recursive algorithm
# sampleArray = [5, 4, 10,...,8, 11, 68, 87, 10]
# A = [11, 4, 12, 7]
# n = 4
# def findMaxNumRec(sampleArray, n): # --- M(n)
#     if n == 1: #---O(1)
#         return sampleArray[0] #--O(1)
#     return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1)) #---M(n-1)

# print(findMaxNumRec(A, 4))

# M(n) = O(1) + M(n-1)
# M(1) = O(1)
# M(n-1) = O(1) + M((n-1) -1)
# M(n-2) = O(1) + M((n-2) -1)

    # M(n) = 1 + M(n-1)
    #      = 1 + (1+M((n-1)-1))
    #      = 2 + M(n-2)
    #      =2+1+M((n-2) -1)
    #      =3+M(n-3)
    #      =a+M(n-a)
    #      =n-1+M(n-(n-1))
    #      =n-1+1
    #      =n

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)