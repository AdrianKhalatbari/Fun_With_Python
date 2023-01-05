def reverse(inputStr):
    return inputStr[::-1]


inputStr = input("Please enter your input:\n")
reverseStr = reverse(inputStr)
if reverseStr == inputStr:
    print("This number is palindrome")
else:
    print("This number is not palindrome")
