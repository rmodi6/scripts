# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        ans = ((1 + 8*n)**0.5) / 2
        if ans - int(ans) >= 0.5:
            ans = int(ans) + 1
        else:
            ans = int(ans)
        return ans - 1
