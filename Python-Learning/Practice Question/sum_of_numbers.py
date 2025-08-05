def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


numbers = int(input("enter the number with commas:"))
print("The sum of the numbers in the list is:", sum_of_numbers(numbers))