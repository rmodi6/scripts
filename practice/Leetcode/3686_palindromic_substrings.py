# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3686/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            l = i
            r = i
            while(l > -1 and r < n and s[l] == s[r]):
                ans += 1
                l -= 1
                r += 1
                        
        for i in range(n):
            l = i
            r = i + 1
            while(l > -1 and r < n and s[l] == s[r]):
                ans += 1
                l -= 1
                r += 1
        return ans
