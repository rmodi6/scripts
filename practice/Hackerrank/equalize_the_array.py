#!/bin/python3
# https://www.hackerrank.com/challenges/equality-in-a-array/problem

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    hmap = {}
    max_count = 0
    for i in arr:
        hmap[i] = hmap.get(i, 0) + 1
        if hmap[i] > max_count:
            max_count = hmap[i]
    return len(arr) - max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
