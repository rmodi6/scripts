# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        x = str(N)
        for i in range(31):
            y = str(2**i)
            if Counter(x) == Counter(y):
                return True
        return False
