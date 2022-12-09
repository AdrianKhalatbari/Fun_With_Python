# A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.
#
# For example, 175 is a Disarium number as follows:
#
# 11+ 72 + 53 = 1+ 49 + 125 = 175


def power(n, power):
    temp = n * n
    for i in range(power - 2):
        temp = temp * n
    return temp


inputNumber = input("Please enter your number: ")
numbList = []
for i in range(len(inputNumber)):
    numbList.append(inputNumber[i])
powered = 0
for i in numbList:
    powered = powered + power(int(i), int(numbList.index(i) + 1))
if powered == int(inputNumber):
    print(inputNumber, 'is a disarium number')
else:
    print(inputNumber, 'is not a disarium number')
