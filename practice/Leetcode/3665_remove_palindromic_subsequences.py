# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return int(s != '') + int(s != s[::-1])
