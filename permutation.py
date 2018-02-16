Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.




#!/bin/python3

import sys
from itertools import permutations

def miniMaxSum(arr):
    b=[]
    perm=permutations(arr,4)
    for i in list(perm):
        b.append(sum(i))
    maxi=max(b)
    mini=min(b)
    print(mini,maxi,end=" ")
        
        
    
    

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
