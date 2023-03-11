"""
A: list to be sorted
"""
def insertionSort(A: list) -> list:
    if (len(A) == 0 or len(A) == 1):
        return A
    for i in range(0, len(A)):
        key = A[i]
        j = i - 1
        while (j >= 0) and (A[j] < key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A


def checkSort(A: list):
    print(f"Unsorted : {A}")
    insertionSort(A)
    print(f"Sorted   : {A}")
    
        
    
list0 = [2,8,7,1,3,5,6,4]
list1 = [0,50,36,48,12,24]
list2 = [0,9,1,2,3,4,5,6,7,10,9]
list3 = [1]
list4 = []

checkSort(list0)
checkSort(list1)
checkSort(list2)
checkSort(list3)
checkSort(list4)
