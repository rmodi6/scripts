# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(list(permutations([str(i+1) for i in range(n)]))[k-1])
