'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_mergesort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_mergesort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_mergesort method would cause 
   the evaluation program error and you will not get credit for your
   submission.


name: Jesus Cerda
studentID: 029148637

assignment:PA1
'''

import sys
import random
import time
import math

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

    def pa1_mergesort (self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)
        
        n = len(query_list)

        # get the start time
        st = time.process_time()
        
        # your merge sort algorithm comes here ...
        def merge(A: list, left: int, mid: int, right: int):
            n1 = mid - left + 1     #Size of left array
            n2 = right - mid        #Size of right array
            L = []; R = [];         #Temp arrays
            for i in range(n1):     #Loading Temp array left
                L.append(A[left+i])
            for j in range(n2):     #Loading Temp array right
                R.append(A[mid+j+1])
            for i in range (n1+n2): #This function merges the two lists, in descending order
                if(len(L) != 0) and (len(R) != 0):
                    if L[0] >= R[0]:    #takes larger of two first values
                        A[i+left] = L.pop(0)
                    else:
                        A[i+left] = R.pop(0)
                elif len(L):            #adds the rest if other list is empty
                    A[i+left] = L.pop(0)
                elif len(R):
                    A[i+left] = R.pop(0)
            return
        def mergeSort(A: list, left: int, right: int):
            #The function divides the array in 2, then repeats on each half
            #mid gets counted as part of the left array
            if left < right:
                mid = math.floor((left + right) / 2)
                mergeSort(A, left, mid)
                mergeSort(A, mid+1, right)
                merge(A, left, mid, right)#the halves should be sorted, they are merged in order
            return
        def mergeSortInit(unsrt: list) -> list:#This function takes the list and calls mergesort on it
            size = len(unsrt)
            if (size==0) or (size==1):
                return unsrt    #returns the list if it's less than 2 elements
            else:
                sorted = mergeSort(unsrt, 0, size-1)    #sorts if its larger than 2
            return sorted
        output = mergeSortInit(query_list)

        # end of merge sort
        
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
    ret = obj.pa1_mergesort(input_type, elements_count, seed)
    print(ret)
