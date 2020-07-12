# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3388/

from numpy import binary_repr

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(binary_repr(n, 32)[::-1], 2)
