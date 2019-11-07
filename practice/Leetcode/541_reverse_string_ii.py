# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        i = 0
        while(i < len(s)):
            j = i + k
            rev = s[i:j][::-1]
            for x in range(len(rev)):
                ans += rev[x]
                x += 1
            i = i + 2 * k
            ans += s[j:i]
        return ans
