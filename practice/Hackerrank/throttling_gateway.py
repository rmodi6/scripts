#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    # Write your code here
    ans = 0
    for i in range(3, len(requestTime)):
        if requestTime[i-3] == requestTime[i]:
            ans += 1
            continue
        if i > 19 and requestTime[i] - requestTime[i-20] < 10:
            ans += 1
            continue
        if i > 59 and requestTime[i] - requestTime[i-60] < 60:
            ans += 1
            continue
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requestTime_count = int(input().strip())

    requestTime = []

    for _ in range(requestTime_count):
        requestTime_item = int(input().strip())
        requestTime.append(requestTime_item)

    result = droppedRequests(requestTime)

    fptr.write(str(result) + '\n')

    fptr.close()
