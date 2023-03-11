import math
"""
A:      The list to be merged
left:   The left element index
right:  The right element index
mid :   The middle element index

The function will merge the elements from "left" to "right"
mid gets counted as part of the left array
"""
def merge(A: list, left: int, mid: int, right: int):
    n1 = mid - left + 1     #Size of left array
    n2 = right - mid        #Size of right array
    L = []; R = [];         #Temp arrays
    for i in range(n1):     #Loading Temp array left
        L.append(A[left+i])
    for j in range(n2):     #Loading Temp array right
        R.append(A[mid+j+1])
    #print(f"{left}, {mid}, {right}")

    for i in range (n1+n2):
        #print(f"{A}, {L}, {R}")
        if(len(L) != 0) and (len(R) != 0):
            if L[0] >= R[0]:
                A[i+left] = L.pop(0)
            else:
                A[i+left] = R.pop(0)
        elif len(L):
            A[i+left] = L.pop(0)
        elif len(R):
            A[i+left] = R.pop(0)
        else:
            print("Something has gone wrong!")
            
    
    return

"""
A:      The list to be merged
left:   The left element, as the actual position (ie: 1 is first element)
right:  The right element, as the actual position (ie: 5 is fifth element)
"""

def mergeSort(A: list, left: int, right: int):
    if left < right:
        mid = math.floor((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, right)
    return

def mergeSortInit(unsrt: list) -> list:
    size = len(unsrt)
    if (size==0) or (size==1):
        return unsrt
    else:
        sorted = mergeSort(unsrt, 0, size-1)
    return sorted

def checkSort(A: list):
    print(f"Unsorted : {A}")
    mergeSortInit(A)
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
