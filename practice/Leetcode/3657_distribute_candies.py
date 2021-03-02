# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(Counter(candyType)))
