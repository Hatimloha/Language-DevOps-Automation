# Function use in list 

# Add item
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
my_list.append("Hatim")
print(my_list)


# Remove item
my_list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
my_list.remove("Orange")
print(my_list)  

# Sort item
list = [5,1,4,6,8,9,3]
list.sort()
print(list)

# reverse item
list = [5,1,4,6,8,9,3]
list.reverse()
print(list)

# Insert in between
list = [5,1,4,6,8,9,3]
list.insert(3, 56)  # _ stand for place, _ for value
print(list) # output: [5,1,4,56,6,8,9,3] 

# pop from list (remove)
# Insert in between
list = [5,1,4,6,8,9,3]
list.pop(4)  # output: [5,1,4,8,9,3]
print(list)