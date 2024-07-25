arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('------------Reverse Order------------')
# Print Array in reversed order
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")

print('\n------------Even Order------------')
# Print Array in even positions
for i in range(1, len(arr), 2):
    print(arr[i], end=" ")

print('\n------------Odd Order------------')
# Print Array in odd positions
for i in range(0, len(arr), 2):
    print(arr[i], end=" ")

print('\n------------Largest Element------------')
# Print Largest Element in Array
temp = 0
for i in arr:
    if i >= temp:
        temp = i
print(temp, end='')

print('\n------------rotate elements of an array------------')
# rotate elements of an array
arr1 = [1, 2, 3, 4, 5]
n = 3
tempList = []
for i in range(n - 1):
    tempList.append(arr1[0])
    arr1.remove(arr1[0])
for j in tempList:
    arr1.append(j)
print(arr1)

print('\n------------array in ascending order------------')
# array in ascending order
arr2 = [5, 2, 8, 7, 1]
for i in range(0, len(arr2)):
    for j in range(i+1, len(arr2)):
        if arr2[i] > arr2[j]:
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp
print(arr2, end='')

print('\n------------array in descending order------------')
# array in descending order
for i in range(0, len(arr2)):
    for j in range(i+1, len(arr2)):
        if arr2[i] < arr2[j]:
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp
print(arr2, end='')

print('\n------------DuplicateElementsOfArray------------')
# Duplicate Elements Of Array
arr3 = [1, 2, 3, 4, 2, 7, 8, 8, 3]
newList = []
for i in arr3:
    if i in newList:
        print(str(i), end=',')
    else:
        newList.append(i)
