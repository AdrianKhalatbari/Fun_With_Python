arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]
newList = []
for i in arr:
    if i in newList:
        print(str(i))
    else:
        newList.append(i)