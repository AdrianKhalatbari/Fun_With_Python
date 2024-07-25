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
for i in range(0, len(arr1)):
    # Find the index of 3
    if arr1[i] == n:
        temp = arr1[i:]
        temp.extend(arr1[:i])
        arr1 = temp
        break
print(arr1)

print('\n------------array in ascending order------------')
# array in ascending order
arr2 = [5, 2, 8, 7, 1]
arr2.sort()

print('\n------------array in descending order------------')
# array in descending order
arr2.sort(reverse=True)
# OR
arr2[::-1]

print('\n------------DuplicateElementsOfArray------------')
# Duplicate Elements Of Array
arr3 = [1, 2, 3, 4, 2, 7, 8, 8, 3]
duplicates = []
arr3.sort()
for i in range(0, len(temp) - 1):
    if temp[i] == temp[i + 1]:
        duplicates.append(temp[i])
print(duplicates)
