# Recursion #
# Recursive function
# def recursiveMethod(n):
#     if(n < 1):
#         print("n is less than 1")
#     else:
#         recursiveMethod(n-1)
#         print(n)

# recursiveMethod(2)

# factorial
# def factorial(n):
#     assert n >= 0 and int(n) == n, "the number must be a positive integer only!"
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(10))

# fibonacchi numbers
# def fibonacci(n):
#     assert n >= 0 and int(n) == n, "Fibonacci number can not be negative or non integer"
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))

# How to find th sum of digits of a positive integer number using recursion
# Step 1 - Recursive case - the flow
# def sumOfDigits(n):
    # Step 3 - unintentional case - the constraint 
    # assert n >= 0 and int(n) == n, "The number must be a positive integer"
    # Step 2 - Base case - the stopping criterion
#     if n == 0:
#         return 0
#     else:
#         return int(n%10) + sumOfDigits(int(n/10))

# print(sumOfDigits(12345))

# How to calculate power of a number using recursion
# Step 1 - Recursive case - the flow
# def power(base, exp):
    # Step 3 - unintentional case - the constraint
    # assert exp >= 0 and int(exp) == exp, "The exponent must be a positive integer only"
    # Step 2 - Base case - the stopping criterion
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     return base * power(base, exp-1)

# print(power(2.2,5))

# How to find GCD(Greatest Commin Devisor) or two numbers using recursion ?
# GCD is the largest positive integer that devide the numbers without any remainder
# def gcd(a,b):
#     assert int(a) == a and int(b) == b, "the number must be integer only"
#     if a < 0:
#         a = -1 * a
#     if b < 0:
#         b = -1 * b
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)

# print(gcd(248, 108))

# How to convert a number from decimal to binary using recursion
#  Recursive case - the flow
# converting decimal to binary
# Devide the nuber by 2
# get the integer quotient for the next iteration
#  get the remainder for the binary digit
#  repeat the step until the quotient is equal to 0
# f(n) = n mod 2 + 10 * f(n/2)
# def decimalToBinary(n):
#     assert int(n) == n, "The parameter must be an iteger only"
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * decimalToBinary(int(n/2))

# print(decimalToBinary(1.2))