# Function related to strings:

# str.upper()
text = "hello"
print(text.upper())  # Output: HELLO

# str.lower()
text = "HELLO"
print(text.lower())  # Output: hello

# str.capitalize()
text = "hello world"
print(text.capitalize())  # Output: Hello world

# str.title()
text = "hello world"
print(text.title())  # Output: Hello World

# str.strip([chars])
text = "   hello   "
print(text.strip())  # Output: hello

text = "***hello***"
print(text.strip('*'))  # Output: hello

# str.replace(old, new)
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python

# str.split([sep])
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

text = "apple,banana,cherry"
print(text.split(','))  # Output: ['apple', 'banana', 'cherry']

# tr.join(iterable)
words = ['hello', 'world']
print(' '.join(words))  # Output: hello world

words = ['apple', 'banana', 'cherry']
print(', '.join(words))  # Output: apple, banana, cherry

# str.find(sub)
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1

# str.startswith(prefix)
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.startswith("world"))  # Output: False


# str.replace(change)
text = "Aman is a good boy"
print(text.replace("good", "bad"))