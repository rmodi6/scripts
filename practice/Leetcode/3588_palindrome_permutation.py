# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3588/

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        k = len(s) % 2
        for ch in c:
            k -= c[ch] % 2
            if k < 0:
                return False
        return True
