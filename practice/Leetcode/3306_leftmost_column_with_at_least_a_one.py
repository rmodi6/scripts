# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r, c = binaryMatrix.dimensions()
        x, y = 0, c-1
        ans = -1
        while x < r and y > -1:
            e = binaryMatrix.get(x, y)
            if e == 0:
                x += 1
            else:
                ans = y
                y -= 1
        return ans
