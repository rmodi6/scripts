# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3471/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scounts = Counter(s)
        tcounts = Counter(t)
        for ch in t:
            if ch not in scounts or tcounts[ch] > scounts[ch]:
                return ch
