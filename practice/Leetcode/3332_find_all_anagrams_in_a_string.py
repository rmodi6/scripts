# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        smap, pmap = Counter(s[:len(p)]), Counter(p)
        if smap == pmap:
            ans.append(0)
        for i in range(len(p), len(s)):
            smap[s[i]] += 1
            if smap[s[i-len(p)]] == 1:
                del smap[s[i-len(p)]]
            else:
                smap[s[i-len(p)]] -= 1
            if smap == pmap:
                ans.append(i - len(p) + 1)
        return ans
