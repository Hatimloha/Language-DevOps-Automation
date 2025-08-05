# Dictionary Methods

# Items funtion use: 
Marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 76
}

print(Marks.items()) # dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 76)])

# keys funtion use: 
Marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 76
}
print(Marks.keys())


# Value funtion use: 
Marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 76
}
print(Marks.values())

# Update funtion use: 
Marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 76
}
Marks.update({"Harry": 55})
print(Marks)

# Update funtion use Example 2: 
Marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 76
}
Marks.update({"Harry": 55, "Rehana": 100}) 
print(Marks) # Output: {'Harry': 55, 'Shubham': 56, 'Rohan': 76, 'Rehana': 100}


# Get funtion use: 
Marks = {
    "Harry" : 100,  
    "Shubham" : 56,
    "Rohan" : 76
}
print(Marks.get("Harry")) # output: 100