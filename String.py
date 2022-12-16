import string
import random

# Sort Words in Alphabetic Order

print('Sort Words in Alphabetic Order:')
my_str = 'I am Mohammad and I am a python developer'
my_str = my_str.split(' ')
my_str.sort()
print(my_str)
print('-----------------------')

# Remove Punctuation from a String
print('Remove Punctuation from a String')
punctuationStr = 'hello ...... this is encrypterd @#$%&*'
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
output = ''
for char in punctuationStr:
    if char not in punctuation:
        output = output + char
print('input is: ', punctuationStr)
print('output is: ', output)
print('-----------------------')

# reverse a string
print('reverse a string')
firstStr = 'Java Developer'
reversedStr = ''
for char in firstStr:
    reversedStr = char + reversedStr
print('input is: ', firstStr)
print('output is: ', reversedStr)
print('-----------------------')

# Convert List to String in Python
print('Convert List to String in Python:')
first_list = ["Python", "Convert", 11, "List", 12, "String", "Method"]
# to print int values, you should conver int to str with map
convertedStr = " ".join(map(str, first_list))
print('input is: ', first_list)
print('output is: ', convertedStr)
print('-----------------------')

# concatenate two strings in Python
print('concatenate two strings in Python:')
str1 = "Hi"
str2 = 'Mohammad'
print('output is: ', " ".join([str1, str2]))
print('-----------------------')

# generate a Random String
print('generate a Random String')
length = 10
ranStr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
print('The randomly generated string is:', ranStr)
print('-----------------------')

# convert Bytes to string
print('convert Bytes to string:')
byteData = b"Lets eat a \xf0\x9f\x8d\x95!"
strData = byteData.decode('UTF-8')
print(strData)
print('-----------------------')