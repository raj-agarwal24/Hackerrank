
def bubble_sort(list1):            #bubble sort function creted

                                    #loop for traversing the list    
    for i in range(0, len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = [3, 6, 9, 12, 15, 18]
print('the unsorted list is: ',list1)
    #function called bubble_sort
print("The sorted list is: ", bubble_sort(list1))