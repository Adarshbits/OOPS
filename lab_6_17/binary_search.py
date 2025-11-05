"""
Binary Search Algorithm
This program implements the binary search algorithm to find an element in a sorted list.
Binary search is an efficient algorithm that works by repeatedly dividing the search interval in half.
Time complexity: O(log n)
"""

l = [1, 2, 3, 4, 5]
key = int(input("Enter key : "))
low = 0
high = len(l) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if l[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif l[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
