#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    answer = -1
    keyboards = sorted(keyboards)
    drives = sorted(drives)
    pointer_low = 0
    pointer_high = len(drives) - 1
    while pointer_low < len(keyboards) and pointer_high > -1:
        s = keyboards[pointer_low] + drives[pointer_high]
        if s == b:
            return b
        elif s < b:
            if s > answer:
                answer = s
            pointer_low += 1
        else:
            pointer_high -= 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
