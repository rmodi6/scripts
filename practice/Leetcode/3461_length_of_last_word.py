# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.rstrip().split()
        return 0 if len(split) < 1 else len(split[-1])
