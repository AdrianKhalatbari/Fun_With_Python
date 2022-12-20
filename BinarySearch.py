def binarysearch(list, n):
    list.sort()
    high = len(list) - 1
    min = 0
    while min <= high:
        mid = int((high + min) / 2)
        if n > list[mid]:
            min = mid + 1
        elif n < list[mid]:
            high = mid - 1
        else:
            return mid
    return -1


def recursivebinarysearch(list, n):
    list.sort()
    high = len(list) - 1
    min = 0
    while min <= high:
        mid = int((high + min) / 2)
        if n > list[mid]:
            min = mid + 1
            recursivebinarysearch(list[min:], n)
        elif n < list[mid]:
            high = mid - 1
            recursivebinarysearch(list[:high], n)
        else:
            return mid
    return -1


list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45
# ////////////////////////////////// Test main def
# result = binarysearch(list1, n)
# ////////////////////////////////// Test Recursive def
result = recursivebinarysearch(list1, n)
if result != -1:
    print("The result is in index: ", str(result))
else:
    print("The element is not in list!")
