# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(s):
            if j == len(t):
                return False
            while s[i] != t[j]:
                j += 1
                if j == len(t):
                    return False
            i += 1
            j += 1
        return i == len(s)
