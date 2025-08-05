# Find the Greatest Common Divisor (GCD)
# The GCD of two integers is the largest positive integer that divides both numbers without a remainder.

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = 48, 18
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")