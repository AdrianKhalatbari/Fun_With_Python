# The pronic number is a product of two consecutive integers of the form: n(n+1).
#
# For example:
# 6 = 2(2+1)= n(n+1),
# 72 =8(8+1) = n(n+1)
#
# Some pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56 etc.
#
# In this program, we need to print all pronic numbers between 1 and userInput
# and check a number(That is pronic or not)

inputNumber = int(input('Please enter number to check:'))


def ponicNumber(searchedNumber):
    output_list = []
    for i in range(1, inputNumber):
        temp = i * (i + 1)
        if temp <= inputNumber:
            output_list.append(temp)
    return output_list


# ////////Print a List of ponic numbers
outputs = ponicNumber(inputNumber)
print(outputs)
if inputNumber in outputs:
    print("Your input is ponic number")
else:
    print('Your input is not ponic number')
