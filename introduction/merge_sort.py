
def merge_sort(list1, left_side, right_side):         # funtion to divide the lists in the two sublists  
    if left_side >= right_side:  
        return  
  
    middle = (left_side + right_side)//2  
    merge_sort(list1, left_side, middle)  
    merge_sort(list1, middle + 1, right_side)  
    merge(list1, left_side, right_side, middle)  

def merge(list1, left_side, right_side, middle):        # Defining a function for merge the list  

    left_sublist = list1[left_side:middle + 1]           # Creating subparts of a lists  
    right_sublist = list1[middle+1:right_side+1]  
  
    # Initial values for variables that we use to keep  
    # track of where we are in each list1  
    left_sublist_side = 0  
    right_sublist_side = 0  
    sorted_side = left_side  
  
    # here we will traverse both copies until we shift out one element  
    while left_sublist_side < len(left_sublist) and right_sublist_side < len(right_sublist):  
  
        # If our left_sublist has the smaller element, put it in the sorted  
        # part and then move forward in left_sublist (by increasing the pointer)  
        if left_sublist[left_sublist_side] <= right_sublist[right_sublist_side]:  
            list1[sorted_side] = left_sublist[left_sublist_side]  
            left_sublist_side = left_sublist_side + 1  
        # Otherwise add it into the right sublist  
        else:  
            list1[sorted_side] = right_sublist[right_sublist_side]  
            right_sublist_side = right_sublist_side + 1  
  
  
        # move forward in the sorted part  
        sorted_side = sorted_side + 1  
  
       
    # we will go through the remaining elements and add them  
    while left_sublist_side < len(left_sublist):  
        list1[sorted_side] = left_sublist[left_sublist_side]  
        left_sublist_side = left_sublist_side + 1  
        sorted_side = sorted_side + 1  
  
    while right_sublist_side < len(right_sublist):  
        list1[sorted_side] = right_sublist[right_sublist_side]  
        right_sublist_side = right_sublist_side + 1  
        sorted_side = sorted_side + 1  
  
list1 = [12, 67, 85, 48, 38, 98, 92, 70, 51, 24, 63]  
merge_sort(list1, 0, len(list1) -1)  
print(list1)  