#insertion_sort function

def insertion_sort(list1):
    
    for i in range(1, len(list1)):

        value = list1[i]
            #move elements 1 place ahead from current place
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1

list1 = [20, 7, 25, 1, 28, 10, 5, 21, 14]
print('The unsorted list is: ', list1)

print('The sorted list is: ', insertion_sort(list1))