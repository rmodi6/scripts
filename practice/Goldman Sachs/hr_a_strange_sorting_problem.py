#!/bin/python3
# Goldman Sachs Internship Coding Question 2

import math
import os
import random
import re
import sys


#
# Complete the 'strangeSort' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY mapping
#  2. STRING_ARRAY nums
#

def strangeSort(mapping, nums):
    # Write your code here
    # print(mapping)
    # print(nums)
    mapp = {}
    for num in nums:
        s = ''
        for digit in num:
            s += str(mapping.index(int(digit)))
        if int(s) not in mapp:
            mapp[int(s)] = []
        mapp[int(s)].append(num)
    actual = sorted(mapp.keys())
    res = []
    for i in actual:
        res.extend(mapp[i])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mapping_count = int(input().strip())

    mapping = []

    for _ in range(mapping_count):
        mapping_item = int(input().strip())
        mapping.append(mapping_item)

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = input()
        nums.append(nums_item)

    result = strangeSort(mapping, nums)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
