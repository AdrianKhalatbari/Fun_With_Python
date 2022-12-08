def power(n, power):
    temp = n * n
    for i in range(power - 2):
        temp = temp * n
    return temp

inputNumber = input("Please enter your number: ")
numbList = []
for i in range(len(inputNumber)):
    numbList.append(inputNumber.__getitem__(i))
powered = 0
for i in numbList:
    powered = powered + power(int(i), int(numbList.index(i) + 1))
if powered == int(inputNumber):
    print(inputNumber, 'is a disarium number')
else:
    print(inputNumber, 'is not a disarium number')
