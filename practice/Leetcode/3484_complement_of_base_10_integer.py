# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3484/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return N ^ (2 ** (len(bin(N)) - 2) - 1)
