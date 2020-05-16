# https://leetcode.com/contest/biweekly-contest-26/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        pc = s[0]
        ans = 1
        count = 1
        for c in s[1:]:
            if c == pc:
                count += 1
            else:
                count = 1
            pc = c
            ans = max(ans, count)
        return ans
