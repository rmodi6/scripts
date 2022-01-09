# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        i, j = 0, 0
        ans = 0
        while j < len(s):
            while s[j] in substr:
                substr.remove(s[i])
                i += 1
            substr.add(s[j])
            ans = max(ans, len(substr))
            j += 1
        return ans
