#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
#Input = [1,1,1,3,3]
#Possible triangles = [1,1,1] and [1,3,3]
#The maximum perimeter is for [1,3,3] = 7
#Output = 1 3 3 
def maximumPerimeterTriangle(sticks):
    # Write your code here
    
    sticks.sort()  # Sort the sticks in ascending order

    for i in range(len(sticks) - 1, 1, -1):
        # Check the triangle inequality: a + b > c
        # sticks[i] is the longest side (c)
        # sticks[i-1] is the middle side (b)
        # sticks[i-2] is the shortest side (a)
        if sticks[i-2] + sticks[i-1] > sticks[i]:
            return [sticks[i-2], sticks[i-1], sticks[i]]

    return [-1]  # No valid triangle found
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
