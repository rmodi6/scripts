# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(n):
            l = i - 1
            r = i + 1
            while(l > -1 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
            max_str = s[l+1:r]
            if len(max_str) > len(ans):
                ans = max_str
                        
        for i in range(n):
            l = i
            r = i + 1
            while(l > -1 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
            max_str = s[l+1:r]
            if len(max_str) > len(ans):
                ans = max_str

        return ans
