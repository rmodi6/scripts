# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(list(map(int, bin(x ^ y)[2:])))
