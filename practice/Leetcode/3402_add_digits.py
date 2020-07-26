# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402/

class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum(map(int, list(str(num)))))
