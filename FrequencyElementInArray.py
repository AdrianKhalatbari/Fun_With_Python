def calculateCharacter(userInput):
    arr = []
    for i in userInput:
        arr.append(i)
    dictionary = {}
    for i in arr:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            temp = dictionary[i]
            dictionary[i] = temp + 1
    return dictionary


userInput = input("Please enter your input:")
print(calculateCharacter(userInput))


# Create a Dictionary of characters
charDict = {}
for i in userInput:
    if i in charDict:
        charDict[i] = charDict[i] + 1
    else:
        charDict[i] = 1
print('Second way: ', charDict)

if charDict == calculateCharacter(userInput):
    print('Both are same')
