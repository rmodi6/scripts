#!/bin/python3
# Goldman Sachs Internship Coding Question 1

import math
import os
import random
import re
import sys


#
# Complete the 'maxLCS' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def maxLCS(s):
    # Write your code here
    ans = 0
    left_map = {}
    right_map = {}
    for ch in s:
        if ch not in right_map:
            right_map[ch] = 0
        right_map[ch] += 1
    for cut_index in range(len(s)):
        common_characters = set(left_map.keys()).intersection(set(right_map.keys()))
        max_common = 0
        for cch in common_characters:
            max_common += min(left_map[cch], right_map[cch])
        ans = max(ans, max_common)
        max_possible_ans = min(cut_index, len(s) - cut_index) + 1
        if ans >= max_possible_ans:
            break
        ch_to_swap = s[cut_index]
        if ch_to_swap not in left_map:
            left_map[ch_to_swap] = 0
        left_map[ch_to_swap] += 1
        right_map[ch_to_swap] -= 1
        if right_map[ch_to_swap] == 0:
            right_map.pop(ch_to_swap)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = maxLCS(s)

    fptr.write(str(result) + '\n')

    fptr.close()
