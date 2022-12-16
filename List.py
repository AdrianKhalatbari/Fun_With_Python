import collections
# Compare two lists in Python
print('#############################################################################')
print('*****Compare two lists in Python*****')


list1 = [11, 12, 13, 14, 15]
list2 = [15, 13, 11, 12, 14]
# 1- The set() function
a = set(list1)
b = set(list2)
print('--------------------------------')
print("Two lists checked with Set().")
if a == b:
    print("The lists are equal.")
else:
    print("The list are not equal.")

# 2- The sort() method
list1.sort()
list2.sort()
print('--------------------------------')
print("Two lists checked with Sort().")
if list1 == list2:
    print("The lists are equal.")
else:
    print("The list are not equal.")

# 3- The collection.counter()
# The collection module provides the counter(), which compare the list efficiently.
# It stores the data in dictionary format <value>:<frequency> and counts the frequency of the list's items
print('--------------------------------')
print("Two lists checked with Collection.counter().")
if collections.Counter(list1) == collections.Counter(list2):
    print("The lists are equal.")
else:
    print("The list are not equal.")

# Convert list to dictionary
print('#############################################################################')
print('*****Convert list to dictionary*****')
# Passed Student:
print('--------------------------------')
print('Convert list to dictionary - Using Dictionary Comprehension')
student = ["James", "Abhinay", "Peter", "Bicky"]
studentDictionary = {s: "passed" for s in student}
print(studentDictionary)

print('--------------------------------')
print('Convert list to dictionary - Using Using zip() function')


# The zip() function is used to zip the two values together.
# First, we need to create an iterator and initialize to any variable and then typecast to the dict() function.
def convert_dict(input):
    init = iter(input)
    resDict = dict(zip(init, init))
    return resDict


list_1 = ['x', 1, 'y', 2, 'z', 3]
print(convert_dict(list_1))
