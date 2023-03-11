'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_quicksort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_quicksort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_quicksort method would cause 
   the evaluation program error and you will not get credit for your
   submission.


name: Jesus Cerda
studentID: 029148637

assignment:PA1
'''
import sys
import random
import time

class Solution:
    
    # this function returns a descending sorted array.
    def function_a (self, elements_count: int) -> list:
        output = []
        for i in range(elements_count,0, -1):
            output.append(i)
        return output

    # this function returns an ascending sorted array.  
    def function_b (self, elements_count: int) -> list:
        output = []
        for i in range(1, elements_count):
            output.append(i)
        return output

    # this function returns a randomly generated array  
    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0,elements_count+1):
            output.append(random.randint(1,1000000))

        return output

    # this function selects a correct action based on the input a, b or c.  
    def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        if input_type == "a":
            output = self.function_a(elements_count)
        if  input_type == "b":
            output = self.function_b(elements_count)
        if  input_type == "c":
            output = self.function_c(elements_count, seed)
        return output   

    def pa1_quicksort (self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)
        
        n = len(query_list)

        # get the start time
        st = time.process_time()
        
        # your quicksort algorithm comes here ...
        def swapInList(A: list, x: int, y: int): #literally just swap
            temp = A[x]
            A[x] = A[y]
            A[y] = temp
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
        def quickSort(A: list, p: int, r: int):
            if(p < r):
                q = partition(A, p, r)  #puts the pivot in its correct spot
                quickSort(A, p, q-1)    #quicksort on left of pivot
                quickSort(A, q+1, r)    #quicksort on right of pivot
            return
        def quickSortInit(unsrt: list) -> list: #This function takes the list and calls quicksort on it
            size = len(unsrt)
            if (size==0) or (size==1):  #returns the list if its 0 or 1 elements
                return unsrt
            else:   #calls quicksort if its larger than 1
                sorted = quickSort(unsrt, 0, size-1)
            return sorted
        output = quickSortInit(query_list)

        # end of quicksort
        
        et = time.process_time()
        res = et - st

        return [query_list, res]




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
    ret = obj.pa1_quicksort(input_type, elements_count, seed)
    print(ret)

