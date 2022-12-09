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
