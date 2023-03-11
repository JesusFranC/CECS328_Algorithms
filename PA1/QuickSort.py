def swapInList(A: list, x: int, y: int):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

"""
This is the partitioning portion, where all the work is done

A: The list to be sorted
r: the pivot and last element of the quicksort
p: The start of the quicksort
"""
def partition(A: list, p: int, r: int) -> int:
    #In this example, x is the pivot and the last element in the array
    x = A[r]
    i = p-1         #i is the last element of the "less than" sub array
    j = p           #j is the first element after the "greater than" sub array
    #loops through the whole section being sorted
    while j < r:
        if A[j] >= x:
            i = i+1
            swapInList(A, i, j)
        j = j+1
    swapInList(A, i+1, r)
    return (i+1)

"""
This is the recursive call, and works on part of the list from index p to r

A: The list to be sorted
r: the pivot and last element of the quicksort
p: The start of the quicksort
"""
def quickSort(A: list, p: int, r: int):
    if(p < r):
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return
def quickSortInit(unsrt: list) -> list:
    size = len(unsrt)
    if (size==0) or (size==1):
        return unsrt
    else:
        sorted = quickSort(unsrt, 0, size-1)
    return sorted

def checkSort(A: list):
    print(f"Unsorted : {A}")
    quickSortInit(A)
    print(f"Sorted   : {A}")
    
        
    
list0 = [2,8,7,1,3,5,6,4]
list1 = [0,50,36,48,12,24]
list2 = [0,1,2,3,4,5,6,7,10,9]
list3 = [1]
list4 = []

checkSort(list0)
checkSort(list1)
checkSort(list2)
checkSort(list3)
checkSort(list4)

