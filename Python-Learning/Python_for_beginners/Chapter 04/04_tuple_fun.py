# 1. count(value)
my_tuple = (1, 2, 3, 1, 1, 4, 5)
# Count occurrences of the value 1
count_of_1 = my_tuple.count(1)
print(count_of_1)  # Output: 3

# 2. index(value, [start, [end]])
my_tuple = (10, 20, 30, 40, 50)
# Find the index of the value 30
index_of_30 = my_tuple.index(30)
print(index_of_30)  # Output: 2
# Find the index of the value 30 within a specific range
index_of_30_in_range = my_tuple.index(30, 1, 4)
print(index_of_30_in_range)  # Output: 2

### 3. Tuple Creation and Indexing
# Create a tuple
my_tuple = ('apple', 'banana', 'cherry')
# Access elements by index
first_element = my_tuple[0]
second_element = my_tuple[1]
print(first_element)  # Output: apple
print(second_element)  # Output: banana
 
### 4. Tuple Slicing
# Create a tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')
# Slice the tuple
sub_tuple = my_tuple[1:4]
print(sub_tuple)  # Output: ('b', 'c', 'd')

### 5. Nested Tuples
# Tuples can contain other tuples, allowing for nested structures.
# Create a nested tuple
nested_tuple = (1, (2, 3), (4, (5, 6)))
# Access nested elements
inner_tuple = nested_tuple[1]
deep_element = nested_tuple[2][1][0]
print(inner_tuple)  # Output: (2, 3)
print(deep_element)  # Output: 5

### 6. Tuple Unpacking
# Create a tuple
person = ('John', 25, 'Engineer')
# Unpack the tuple
name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Engineer

### 7. Converting Between Tuples and Lists
# Convert tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
# Convert list to tuple
my_list = [4, 5, 6]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (4, 5, 6)

### 8. Tuple with Single Element
# To create a tuple with a single element, include a trailing comma.
# Example:
# Single element tuple
single_element_tuple = (5,)
print(single_element_tuple)  # Output: (5,)

# Not a tuple
not_a_tuple = (5)
print(not_a_tuple)  # Output: 5