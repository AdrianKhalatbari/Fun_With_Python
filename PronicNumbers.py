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
    flag = False
    output = 0
    ponicNumberList = []
    for i in range(searchedNumber):
        output = (i + 1) * (i + 2)
        if output < searchedNumber:
            ponicNumberList.append(output)
        elif output == searchedNumber:
            flag = True
            ponicNumberList.append(output)
        else:
            return ponicNumberList, flag


# ////////Print a List of ponic numbers
outputs = ponicNumber(inputNumber)[0]
flag = ponicNumber(inputNumber)[1]
print(outputs)
if flag:
    print("Your input is ponic number")
else:
    print('Your input is not ponic number')
