# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i**2 == num:
                return True
            if i**2 > num:
                return False
