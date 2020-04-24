#!/bin/python3
# https://www.hackerrank.com/contests/hacktheinterview3/challenges/distribution-in-m-bins/problem

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    # Write your code here
    a = sorted(a)
    ans = 0
    for i in range(int(len(a)/m)):
        ans += (i+1) * sum(a[i*m:(i+1)*m])
    ans += (i+1) * sum(a[(i+1)*m:])
    return ans % (10**9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)

    fptr.write(str(ans) + '\n')

    fptr.close()
