# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3479/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1, min2, min1_idx = float('inf'), float('inf'), -1
        max1, max2, max1_idx = float('-inf'), float('-inf'), -1
        for i, arr in enumerate(arrays):
            if arr[0] < min2:
                if arr[0] < min1:
                    min2 = min1
                    min1 = arr[0]
                    min1_idx = i
                else:
                    min2 = arr[0]
            if arr[-1] > max2:
                if arr[-1] > max1:
                    max2 = max1
                    max1 = arr[-1]
                    max1_idx = i
                else:
                    max2 = arr[-1]
        if min1_idx != max1_idx:
            return max1 - min1
        else:
            return max(max2 - min1, max1 - min2)
