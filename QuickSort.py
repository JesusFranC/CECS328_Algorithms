def swapInList(A: list, x: int, y: int):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def partition(A: list, p: int, r: int) -> int:
    #In this example, x is the pivot and the last element in the array
    x = A[r]
    print(x)
    i = p-1
    j = p
    #loops through the whole section being sorted
    while j < r-1:
        if A[j] <= x:
            i = i+1
            swapInList(A, i, j)
        j = j+1
    swapInList(A, i+1, r)
    return (i+1)
    
    return
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
    print('[', end='')
    for val in A:
        print(f"{val},", end='')
    print(']')
    quickSortInit(A)
    print('[', end='')
    for val in A:
        print(f"{val},", end='')
    print(']')
    
        
    
list0 = [2,8,7,1,3,5,6,4]
list1 = [0,50,36,48,12,24]
list2 = [0,1,2,3,4,5,6,7,10,9]
list3 = [1]
list4 = []
quickSortInit(list1)
print('[', end='')
for val in list1:
    print(f"{val},", end='')
print(']')
'''
checkSort(list1)
checkSort(list2)
checkSort(list3)
checkSort(list4)
'''
