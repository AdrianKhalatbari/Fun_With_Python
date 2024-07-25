# A number is said to be the Disarium number when the sum of its digit raised
# to the power of their respective positions
# becomes equal to the number itself.
#
# For example, 175 is a Disarium number as follows:
#
# 1^1+ 7^2 + 5^3 = 1+ 49 + 125 = 175

#  First solution
def is_disarium_number(num):
    temp = num
    sum = 0
    length = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** length
        length = length - 1
        temp = temp // 10
    if sum == num:
        return True
    else:
        return False


# Second solution
temp = 0
for i in range(len(str(175))):
    temp = temp + pow(int(str(175)[i]), i + 1)
if temp == 175:
    print('175 is a Disarium number')
