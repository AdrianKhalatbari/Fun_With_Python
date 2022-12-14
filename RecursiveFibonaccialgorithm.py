def Fibo(n):
    if n <= 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)


nterms = int(input("Give a nonnegative integer:\n"))
if nterms <= 1:
    print("Plese enter a positive integer")
else:
    print("Fibo(" + str(nterms) + ") returns " + str(Fibo(nterms)))
