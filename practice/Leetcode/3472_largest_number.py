# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp_func(x, y):
            i = 0
            while i < len(x) and i < len(y):
                if x[i] != y[i]:
                    return int(x[i]) - int(y[i])
                i += 1
            return int(x + y) - int(y + x)
        
        ans = ''.join(sorted(map(str, nums), key=cmp_to_key(cmp_func), reverse=True))
        return str(int(ans))
