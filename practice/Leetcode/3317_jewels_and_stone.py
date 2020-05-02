# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hset = set(list(J))
        count = 0
        for s in S:
            if s in hset:
                count += 1
        return count
