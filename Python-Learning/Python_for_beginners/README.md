# Creating a Markdown file with Python functions, descriptions, and examples

## content
### Python Built-in Functions
> This document contains a list of commonly used Python built-in functions with descriptions and examples.

## 1. **len()**
- **Description**: Returns the number of items in an object (e.g., string, list, tuple, etc.).
- **Syntax**: `len(object)`
- **Example**:
  ```python
  my_list = [1, 2, 3]
  print(len(my_list))  # Output: 3
  ```
  
## 2. **split()**
Description: Splits a string into a list of substrings based on a delimiter.
Syntax: string.split(delimiter)
Example:
```python
text = "Hello World"
print(text.split())  # Output: ['Hello', 'World']
```

## 3. **append()**
Description: Adds an item to the end of a list.
Syntax: list.append(item)
Example:
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

## 4. **remove()**
Description: Removes the first occurrence of a specified value from a list.
Syntax: list.remove(value)
Example:
```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
```

## 5. **list()**
Description: Creates a list from an iterable (e.g., string, tuple, etc.).
Syntax: list(iterable)
Example:
```python
my_tuple = (1, 2, 3)
print(list(my_tuple))  # Output: [1, 2, 3]
```

## 6. **max()**
Description: Returns the largest item in an iterable or among arguments.
Syntax: max(iterable) or max(arg1, arg2, ...)
Example:
```python
numbers = [1, 2, 3, 4]
print(max(numbers))  # Output: 4
```

## 7. **min()**
Description: Returns the smallest item in an iterable or among arguments.
Syntax: min(iterable) or min(arg1, arg2, ...)
Example:
```python
numbers = [1, 2, 3, 4]
print(min(numbers))  # Output: 1
```

## 8. **sorted()**
Description: Returns a sorted list from the elements of an iterable.
Syntax: sorted(iterable, key=None, reverse=False)
Example:
```python
numbers = [4, 2, 1, 3]
print(sorted(numbers))  # Output: [1, 2, 3, 4]
```

## 9. **range()**
Description: Generates a sequence of numbers.
Syntax: range(start, stop, step)
Example:
```python
for i in range(1, 5):
    print(i)  # Output: 1, 2, 3, 4
```

## 10. **type()**
Description: Returns the type of an object.
Syntax: type(object)
Example:
```python
num = 5
print(type(num))  # Output: <class 'int'>
```

## 11. **input()**
Description: Reads a line of text input from the user.
Syntax: input(prompt)
Example:
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

## 12. **sum()**
Description: Adds all items in an iterable.
Syntax: sum(iterable, start=0)
Example:
```python
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6
```

## 13. **map()**
Description: Applies a function to all items in an iterable.
Syntax: map(function, iterable)
Example:
```python
def square(x):
    return x * x

numbers = [1, 2, 3]
print(list(map(square, numbers)))  # Output: [1, 4, 9]
```

## 14. filter()
Description: Filters items in an iterable based on a function.
Syntax: filter(function, iterable)
Example:
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4]
print(list(filter(is_even, numbers)))  # Output: [2, 4]
```

## 15. zip()
Description: Combines multiple iterables into tuples.
Syntax: zip(iterable1, iterable2, ...)
Example:
```python
names = ['Alice', 'Bob']
scores = [85, 90]
print(list(zip(names, scores)))  # Output: [('Alice', 85), ('Bob', 90)]
```

## 16. enumerate()
Description: Adds an index to each item in an iterable.
Syntax: enumerate(iterable, start=0)
Example:
```python
fruits = ['apple', 'banana']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

## 17. round()
Description: Rounds a number to a specified number of decimal places.
Syntax: round(number, ndigits)
Example:
```python
print(round(3.14159, 2))  # Output: 3.14
```
