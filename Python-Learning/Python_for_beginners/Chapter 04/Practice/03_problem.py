# Proof tuple is imutable

my_tuple = (50, 35, 56, "hatim")
my_tuple[2] = "Youtube"     # We are trying to replace the the 3 item with youtube (56 -> youtube)
# Output: TypeError: 'tuple' object does not support item assignment