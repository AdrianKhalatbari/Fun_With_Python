a = int(input("Enter the lower limit of the range:\n"))
b = int(input("Enter the upper limit of the range:\n"))
checkPoint = False
for number in range(a, b + 1):
    if int(number) % 5 != 0:
        print(str(number) + " is NOT divisible by 5.")
    elif int(number) % 5 == 0 and int(number) % 7 != 0:
        print(str(number) + " is NOT divisible by 7.")
    elif int(number) % 5 == 0 and int(number) % 7 == 0:
        print("The number " + str(number) + " is divisible by 5 and 7.")
        print("stopping the search")
        checkPoint = True
        break
if checkPoint == False:
    print('Not found')
