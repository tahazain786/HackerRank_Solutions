#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    l1 = []
    luck = 0
    for i in range(len(contests)):
            if contests[i][1] == 1:
                l1.append(contests[i][0])
            else:
                luck += contests[i][0]
    l1.sort()
    if len(l1) >k:
        for i in range(len(l1)-k):
            luck -= l1[i]
        for i in range(len(l1)-k,len(l1)):
            luck += l1[i]
    elif len(l1) < k:
        for i in range(len(l1)):
            luck += l1[i]
    return luck
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
