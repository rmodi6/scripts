# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

from random import random

class Solution:

    def __init__(self, w: List[int]):
        self.cumsums = []
        cumsum = 0
        for n in w:
            cumsum += n
            self.cumsums.append(cumsum)

    def pickIndex(self) -> int:
        t = self.cumsums[-1] * random()
        for i, cumsum in enumerate(self.cumsums):
            if t < cumsum:
                return i

        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()