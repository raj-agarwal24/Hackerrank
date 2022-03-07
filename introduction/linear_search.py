def linear_search(list1, n, ket):
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1

list1 = [0, 1, 2, 4, 6, 8]
key = 7

n = len(list1)
res = linear_search(list1, n, key)
if(res == -1):
    print("element not found")
else:
    print("element found at index", res)