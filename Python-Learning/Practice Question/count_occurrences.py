# Count Occurrences of an Element in a List
# This algorithm counts how many times a specific element appears in a list.

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
    

lst = [1, 2, 2, 3, 4, 2, 5]
element = 2
print(f"The element {element} appears {count_occurrences(lst, element)} times in the list.")