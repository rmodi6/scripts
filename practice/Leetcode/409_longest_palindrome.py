# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        ans = 0
        for c in counts:
            v = counts[c]
            ans += v - (v % 2)
        return min(ans + 1, len(s))
