# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in bin(n)[2:]:
            ans += int(i)
        return ans
