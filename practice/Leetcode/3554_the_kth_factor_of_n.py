# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        ans = None
        while k > 0 and i <= n:
            if n % i == 0:
                k -= 1
                ans = i
            i += 1
        return ans if k == 0 and ans else -1
