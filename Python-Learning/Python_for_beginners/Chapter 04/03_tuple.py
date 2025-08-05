# Tuple is immutable which mean we can't change the value's like the list
a = (1,2,3,4,5)
print(a)

# Example
list = (1,2,3,4,5)
list.remove(3) # AttributeError: 'tuple' object has no attribute 'remove'
print(a)