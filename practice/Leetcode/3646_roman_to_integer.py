# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/

class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sub = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        ans = 0
        pc = None
        for ch in s[::-1]:
            if ch in sub and pc in sub[ch]:
                ans -= hmap[ch]
            else:
                ans += hmap[ch]
            pc = ch
        return ans
