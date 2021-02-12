# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 2 == 0:
            return self.numberOfSteps(num//2) + 1
        else:
            return self.numberOfSteps(num-1) + 1
