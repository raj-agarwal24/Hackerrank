# program of recursive binary search

def binary_search(list1, low, mid, high, n):
    
    if low <= high:                 # check bottom for recusive function
        mid = (low + high) // 2

        if list1[mid] == n:         # if entered element is at mid itself then return its index
            return mid

        elif list1[mid] > n:        # if element is smaller than the mid value then move left
            return binary_search(list1, low, mid - 1, n)

        else:                       # else move right
            return binary_search(list1, mid + 1, high, n)

    else:                           # element is not available in the list
        return -1

list1 = [11, 22, 34, 45, 68, 79]
n = 34

res = binary_search(list1, 0, len(list1)-1, n)
if res != -1:
    print("Element is at index",str(res))
else:
    print("Element is not present in list1")