# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        n = 1
        while n <= num:
            i = 0
            while i < n and i + n <= num:
                ans.append(ans[i] + 1)
                i += 1
            n = n << 1
        return ans
