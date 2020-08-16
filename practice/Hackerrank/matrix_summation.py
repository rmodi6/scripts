#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findBeforeMatrix' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY after as parameter.
#

def findBeforeMatrix(after):
    # Write your code here
    r, c = len(after), len(after[0])
    before = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            top, left, topleft = 0, 0, 0
            if i > 0:
                top = after[i-1][j]
            if j > 0:
                left = after[i][j-1]
            if i > 0 and j > 0:
                topleft = after[i-1][j-1]
            before[i][j] = after[i][j] - top - left + topleft
    return before

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    after_rows = int(input().strip())
    after_columns = int(input().strip())

    after = []

    for _ in range(after_rows):
        after.append(list(map(int, input().rstrip().split())))

    result = findBeforeMatrix(after)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
