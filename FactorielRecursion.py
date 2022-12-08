def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n * (recur_factorial(n - 1))


number = int(input('Please enter the number:'))
print('the factoriel is:', recur_factorial(number))
