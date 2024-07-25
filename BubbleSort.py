# Concept of Bubble Sort
# The bubble sort uses a straightforward logic that works by
# repeating swapping the adjacent elements if they are not in the right order.
# It compares one pair at a time and swaps if the first element is greater 
# than the second element; otherwise, move further to the next pair of
# elements for comparison.

def bubblesort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
    return list


list1 = [5, 3, 8, 6, 7, 2]
print(bubblesort(list1))
