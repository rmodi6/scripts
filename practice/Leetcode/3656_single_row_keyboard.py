# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3656/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        for i, ch in enumerate(keyboard):
            hmap[ch] = i
        i = ans = 0
        for ch in word:
            ans += abs(i - hmap[ch])
            i = hmap[ch]
        return ans
