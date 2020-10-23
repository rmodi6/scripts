# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3503/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, h = 0, 9999
        while l <= h:
            m = l + (h-l)//2
            v = reader.get(m)
            if v == target:
                return m
            if target < v:
                h = m - 1
            else:
                l = m + 1
        return -1
