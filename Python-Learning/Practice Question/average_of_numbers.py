# Finding the Average of Numbers
# This algorithm calculates the average of numbers in a list.

def average_of_numbers(numbers):
    if len(numbers) == 0:
        return "The lsit is empty."
    total = sum(numbers)
    return total / len(numbers)

numbers = [4, 8, 15, 16, 23, 42]
print(f"The average of the number in the list is:", average_of_numbers(numbers))
