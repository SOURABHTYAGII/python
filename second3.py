# Python program to demonstrate
# string slicing
# String slicing
String = 'ASTRING'
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print(String[s1])
print(String[s2])
print(String[s3])
# String slicing
#         0123456789..12
String = 'GEEKSFORGEEKS'

# Using indexing sequence
print(String[1:8:3])
print(String[1:3:4])