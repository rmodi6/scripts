#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countStrings(s):
    # Write your code here
    count = 0
    for i in range(len(s)):
        count = count + int(s[i] == s[i-1])
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = countStrings(s)

    fptr.write(str(result) + '\n')

    fptr.close()
