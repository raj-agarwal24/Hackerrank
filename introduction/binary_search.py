# Binary search function 


def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:              # value is available in list
        mid = (high + low) // 2

    if list1[mid] < n:                  # check if n is from mid
        low = mid + 1

    elif list1[mid] > n:                # check if n is greater compare to the right of the mid
        high = mid - 1

    else:                               # check if n is smaller compare to the left of the mid    
        return mid

    return - 1                      # value is not available in list


list1 = [11, 22, 34, 45, 68, 79]    # initial list
n = 45

result = binary_search(list1, n)    # function call
if result != -1:
    print ("element is available in inder",str(result))
else:                               # check if n is
    print ("element is not available in list1")