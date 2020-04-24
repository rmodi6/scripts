#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res = []
    scores = sorted(list(set(scores)), reverse=True)
    i, j = 0, len(scores) - 1
    while i < len(alice):
        if j < 0:
            res.append(1)
            i += 1
        elif alice[i] < scores[j]:
            res.append(j + 2)
            i += 1
        elif alice[i] == scores[j]:
            res.append(j + 1)
            i += 1
        else:
            j -= 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
