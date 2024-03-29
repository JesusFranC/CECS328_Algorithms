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

def simpleTest():
    arr = [10,6,2,4,8,12]
    print("Array = ",end='')
    print(*arr, sep=", ", end="\n")
    for i in range(1,len(arr)+1):
        print(f"K = {i}")
        val = kthSmallest(arr, i)
        print(f"Result = {val}\n")

    













    
