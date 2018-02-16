You are in-charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning  years old, and the cake will have  candles of height 3,2 ,1 ,3 , she will be able to blow out  candles successfully, since the tallest candle is of height  and there are  such candles.

Complete the function birthdayCakeCandles that takes your niece's age and an integer array containing height of each candle as input, and return the number of candles she can successfully blow out.



#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    count=0
    a=max(ar)
    for i in ar:
        if i==a:
            count=count+1
        else:
            continue
    return count
            
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
