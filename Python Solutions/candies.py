#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
#Input = [2,4,2,6,1,7,8,9,2,1]
#Here originally all the students have 1 candy [1,1,1,1,1,1,1,1,1,1]
#The second student had more score than first student, so an extra candy is given to the second student
#Output = 19 candies required to buy
def candies(n, arr):
    # Write your code here
    l = n* [1]
    
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            l[i] = l[i-1] + 1
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1]:
            l[i] = max(l[i],l[i+1] + 1)
    return sum(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
