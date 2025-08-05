def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
        return total
    

input_str = input("Enter the number in with commas:")

numbers = [int(x.strip()) for x in input_str.split(',')]

print("The sum of the number in the list is:",sum_of_numbers(numbers))