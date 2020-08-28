# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(reversed(s)):
            v = ord(ch) - 64
            ans += 26**i * v
        return ans
