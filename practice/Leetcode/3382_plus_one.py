# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3382/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         return list(str(int(''.join(list(map(str, digits)))) + 1))
