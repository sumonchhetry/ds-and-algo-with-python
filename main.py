# Recursion #
# Recursive function
def recursiveMethod(n):
    if(n < 1):
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(2)

# factorial
def factorial(n):
    assert n >= 0 and int(n) == n, "the number must be a positive integer only!"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

# fibonacchi numbers
def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number can not be negative or non integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))