# Factorial of a Number
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. This algorithm computes the factorial.


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n +1):
        result *= i
    return result


number = 5
print(f"The factorial of {number} is: {factorial(number)} ")