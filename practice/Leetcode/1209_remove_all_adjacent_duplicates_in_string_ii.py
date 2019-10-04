# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        recheck = True
        while recheck:
            i = 0
            d = 0
            recheck = False
            while i < len(s):
                if i > 0 and s[i] == s[i-1]:
                    d += 1
                else:
                    d = 1
                if d == k:
                    s = s[:i-k+1] + s[i+1:]
                    i -= k
                    d = 0
                    recheck = True
                i += 1
        return s