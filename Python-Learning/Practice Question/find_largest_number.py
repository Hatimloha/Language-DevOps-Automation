def find_largest_number(numbers):
    if not numbers:
        return "the list is empty."
    
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest


number = [3,5,7,2,8,6]
print("the largest number in the list is:", find_largest_number(number))
