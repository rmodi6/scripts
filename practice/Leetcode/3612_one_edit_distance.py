# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3612/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        if len(s) == len(t):
            c = 0
            for i in range(len(s)):
                c += int(s[i] != t[i])
                if c > 1:
                    return False
            return True
        if len(t) > len(s):
            s, t = t, s
        i, j, c = 0, 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                c += 1
                if c > 1:
                    return False
                i += 1
            else:
                i += 1
                j += 1
        return True
