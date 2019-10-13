# https://leetcode.com/contest/weekly-contest-158/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        i = 0
        c = 0
        while i < len(s):
            if s[i] == 'R':
                c += 1
            if s[i] == 'L':
                c -= 1
            if c == 0:
                ans += 1
            i += 1
        return ans
