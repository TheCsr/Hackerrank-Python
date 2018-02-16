Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to n , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .




#!/bin/python3

import sys

def staircase(n):
    for i in range(n-1,-1,-1):
        a=i
        while i!=0:
            print(end=" ")
            i=i-1
        while a!=n:
            print('#',end='')
            a=a+1
        print('')   
    
    

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
