# Fibonacci Sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. This algorithm generates the Fibonacci sequence up to a given number of terms.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


terms = 10
print(f"The first {terms} terms of the Fibonacci sequence are:", fibonacci(terms))