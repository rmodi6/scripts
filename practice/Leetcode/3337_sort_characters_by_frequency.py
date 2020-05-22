# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        scount = Counter(s)
        sorted_scount = sorted(scount, key=lambda k: scount[k], reverse=True)
        ans = ''
        for c in sorted_scount:
            ans += c * scount[c]
        return ans
