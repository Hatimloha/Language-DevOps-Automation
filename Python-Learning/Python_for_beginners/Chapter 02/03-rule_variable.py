# In Python, variables are used to store data values. Variables are created when you assign a value to them. The rules for naming variables in Python are:

# 1. Names Must Begin with a Letter or Underscore: Variable names must start with a letter (a-z, A-Z) or an underscore (_). They cannot start with a digit.
my_variable = 10
_my_variable = 20

# 2. Subsequent Characters: After the initial letter or underscore, the variable name can include letters, digits (0-9), and underscores.
my_variable1 = 30
variable_2 = 40

# 3. Case Sensitivity: Variable names are case-sensitive. This means myvariable, MyVariable, and MYVARIABLE would be considered three different variables.
myvariable = 50
MyVariable = 60
MYVARIABLE = 70

# 4. No Reserved Words: You cannot use Python's reserved words (keywords) as variable names. These are words that Python uses for its syntax and have special meanings, such as class, if, while, import, etc.
# This will raise an error
# class = 80
# Correct usage
my_class = 80

# 5. Descriptive Names: While not a strict rule, it's a good practice to use descriptive names for variables to make your code more readable.
student_age = 21
total_price = 99.99

# 6. Avoid Special Characters and Spaces: Variable names cannot contain spaces or special characters (e.g., !, @, #, $, etc.). Use underscores to separate words in variable names if needed.
# This will raise an error
# my variable = 90
# Correct usage
my_variable = 90

# Example
# Valid variable names
user_name = "Alice"
age = 25
average_score = 88.5
_is_active = True

# Invalid variable names
# 1user = "Bob"     # Starts with a digit
# my variable = "Carol"  # Contains a space
# class = "Math"    # Reserved word
# my-variable = "Dave"  # Contains a special character (hyphen)
