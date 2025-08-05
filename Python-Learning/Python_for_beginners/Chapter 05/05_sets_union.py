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
