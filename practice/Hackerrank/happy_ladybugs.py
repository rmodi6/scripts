# https://www.hackerrank.com/challenges/happy-ladybugs/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def isHappy(b):
    _b = '_' + b + '_'
    for i in range(len(_b)):
        if _b[i] != '_' and _b[i] != _b[i-1] and _b[i] != _b[i+1]:
            return False
    return True

def happyLadybugs(b):
    if isHappy(b):
        return 'YES'
    c = Counter(b)
    if c['_'] > 0:
        del c['_']
        if min(c.values()) > 1:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
