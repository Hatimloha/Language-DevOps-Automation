# type_casting

a = 31
t = type(a)
print(t)  # Output: <Class 'int'>

a = 31.2
t = type(a)
print(t)  # Output: <Class 'float'>

a = "Hatim"
t = type(a)
print(t)  # Output: <Class 'String'>

a = "31.5"
t = type(a)
print(t)  # Output: <Class 'String'> #important

# Change data type
a = "31.5"
b = float(a)
t = type(a)
print(t)  # Output: <Class 'float'> 