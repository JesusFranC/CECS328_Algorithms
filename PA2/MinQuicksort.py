'''
name: Jesus Cerda
studentID: 029148637

assignment:PA2
'''

def swapInList(A: list, x: int, y: int):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

"""
This is the partitioning portion, where we take a the "pivot" and put it in the right spot
All elements left of pivot are smaller, and all elements right of pivot are bigger

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
        if A[j] <= x:               #If current val is less than pivot
            i = i+1                 #Add a value to less than sub array
            swapInList(A, i, j)     #moves item into less than sub array
        j = j+1                     #index to be looked at moves
    swapInList(A, i+1, r)           #Moves pivot into place
    return (i+1)

"""
Looks for the k-th position in the array. Uses the partition function to simplify this process.
Essentially works like quicksort, but does not sort the whole array
It strategically sorts parts of the array, the left OR right partition, until the "pivot" is the kth element

arr:    The array to be sorted
l:      The left  node in partition
r:      The right node in partition
k:      The position we are looking for
"""
def QuickFindK(arr: list, l: int, r: int, k: int)-> int:
    n = len(arr)
    q = -1       #This will be the position of the "pivot". NOTE: The value -1 should never be returned
    if (k > 0) and (k <= n):        #if the "pivot" is within the range of the array
        #print(f"partitioning from {l} to {r}")
        q = partition(arr, l, r)
        #print(f"pivot found at {q}")
    if (q == k-1):                  #if the "pivot" is the same as the position we are looking for
        return arr[q]
    if (q < k-1):                           #if the "pivot" is lower than the position we are looking for
        return QuickFindK(arr, q+1, r, k)
    return QuickFindK(arr, l, q-1, k)      #if the "pivot" is higher than the position we are looking for

"""
This is the main calling function to find the kth Smallest element
it takes the list and the "k-th element" as an input, then returns the value as an integer
Returns a None Value if an Out-Of-Bounds K value is given

arr:    The array to be searched
k:      The value of element to be found

"""
def kthSmallest(arr: list, k: int):
    #Do not bother searching if out of bounds
    if k < 1 or k > len(arr):
        return None
    
    #"If" statements to quickly handle small(0 or 1) list cases
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    return QuickFindK(arr, 0, len(arr)-1, k)

def testProgram():
    arr1 = [1,2,3,4,5]
    k1 = 3
    arr2 = [8,6,4,2,0]
    k2 = 2
    arr3 = [10,6,2,4,8]
    k3 = 5
    arr4 = [5]
    k4 = 1
    arr5 = [0]
    k5 = 0
    
    print("Test case 1 = ", end='')
    print(*arr1, sep = ", ", end=' ')
    print(f"With k value {k1}\n")
    val = kthSmallest(arr1, k1)
    print(f"Result = {val}\n")

    print("Test case 2 = ", end='')
    print(*arr2, sep = ", ", end=' ')
    print(f"With k value {k2}\n")
    val = kthSmallest(arr2, k2)
    print(f"Result = {val}\n")

    print("Test case 3 = ", end='')
    print(*arr3, sep = ", ", end=' ')
    print(f"With k value {k3}\n")
    val = kthSmallest(arr3, k3)
    print(f"Result = {val}\n")

    print("Test case 4 = ", end='')
    print(*arr4, sep = ", ", end=' ')
    print(f"With k value {k4}\n")
    val = kthSmallest(arr4, k4)
    print(f"Result = {val}\n")

    print("Test case 5 = ", end='')
    print(*arr5, sep = ", ", end=' ')
    print(f"With k value {k5}\n")
    val = kthSmallest(arr5, k5)
    print(f"Result = {val}\n")
    return

def simpleTest():
    arr = [10,6,2,4,8,12]
    print("Array = ",end='')
    print(*arr, sep=", ", end="\n")
    for i in range(1,len(arr)+1):
        print(f"K = {i}")
        val = kthSmallest(arr, i)
        print(f"Result = {val}\n")
    

if __name__ == '__main__':
    #testProgram()
    simpleTest()

