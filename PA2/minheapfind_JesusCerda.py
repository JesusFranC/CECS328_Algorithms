'''
name: Jesus Cerda
studentID: 029148637

assignment:PA2
'''
import math

def swapInList(A: list, x: int, y: int):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

"""
Min heapify will ensure the heap condition is met, is the style of a minHeap
The smaller of the two child nodes will rise to the top, and it will then heapify the affected child node

arr:    The array to be heapified
i:      The "Root" to start the heapifying on
"""

def minHeapify(arr, i):
    n = len(arr)
    l = i*2+1
    r = i*2+2
    minim = i
    if(l < n) and (arr[l] < arr[minim]):
        minim = l
    if(r < n) and (arr[r] < arr[minim]):
        minim = r
    if minim != i:
        swapInList(arr, i, minim)
        minHeapify(arr, minim)

def buildMinHeap(arr):
    if len(arr) == 0:
        return
    LPN = math.floor(len(arr)/2) #finding the Last Parent Node
    for i in range(1, LPN+1):
        root = LPN-i
        minHeapify(arr, root)

def kthSmallest(rawArr: list, k:int):
    arr = []
    for val in rawArr:
        arr.append(val)
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    elif k > len(arr):
        return None
    
    buildMinHeap(arr)
    val = None
    for i in range(0,k):
        val = arr.pop(0)
        buildMinHeap(arr)
    return val



if __name__ == '__main__':

    # the input type is either a, b or c 
    # corresponding to function_a, function_b and functin_c.
    input_type = sys.argv[1]

    elements_count = int(sys.argv[2])

    # input seed as 2, so we have the same randomly 
    # generated array.
    # you can change it for your testing.
    seed = sys.argv[3]
    
    obj = Solution()
    # the return value is an array of array.
    ret = obj.pa1_insertionsort(input_type, elements_count, seed)
    print(ret)















