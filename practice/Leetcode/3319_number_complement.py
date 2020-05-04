# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

from numpy import binary_repr

class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (pow(2, len(binary_repr(num)))-1)
