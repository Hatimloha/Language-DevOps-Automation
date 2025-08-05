# Print the sets with the type: 
s = {1,4,5,67,6,75,4,1} # sets will only carry the unique items
print(s, type(s))

# 1. Add: 
s = {1,4,5,67,6,75,4,1} # sets will only carry the unique items
s.add(566)
print(s)

# 2. Removing Elements
s.remove(2)       # Removes an element; raises KeyError if the element is not present
s.discard(3)      # Removes an element; does nothing if the element is not present
s.pop()           # Removes and returns an arbitrary element; raises KeyError if the set is empty
s.clear()         # Removes all elements from the set

# 3. Checking for Membership
2 in s            # Returns True if 2 is in the set, otherwise False

# 4. Set Operations
# Union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union_set = s1.union(s2)  # {1, 2, 3, 4, 5}
# or
union_set = s1 | s2

# Intersection
intersection_set = s1.intersection(s2)  # {3}
# or
intersection_set = s1 & s2

# Difference
difference_set = s1.difference(s2)  # {1, 2}
# or
difference_set = s1 - s2

# Symmetric Difference
symmetric_diff_set = s1.symmetric_difference(s2)  # {1, 2, 4, 5}
# or
symmetric_diff_set = s1 ^ s2

# Subset
s1.issubset(s2)  # Returns True if all elements of s1 are in s2

# Superset
s1.issuperset(s2)  # Returns True if all elements of s2 are in s1

# Disjoint Sets
s1.isdisjoint(s2)  # Returns True if s1 and s2 have no elements in common

# 5. Copying a Set
s_copy = s.copy()  # Returns a shallow copy of the set

# 6. Iterating Over a Set
for elem in s:
    print(elem)

# 7. len(s)  # Returns the number of elements in the set
len(s)  # Returns the number of elements in the set

