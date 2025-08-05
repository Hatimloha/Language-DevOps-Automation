# List 
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(my_list)

# Print any 1 out of list item:
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(my_list[0]) # Output: Apple


# Change the item 
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
my_list[1] = "Banana"
print(my_list) # Output Oranage will replace by Banana

# Print number of string in list
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(my_list[1:4]) # Output: ['Orange', 5, 345.06]

# For loop
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
for item in my_list:
    print(item)
