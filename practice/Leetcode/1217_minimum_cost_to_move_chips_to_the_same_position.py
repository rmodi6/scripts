# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        arr = [0, 0]
        for i in range(len(position)):
            arr[position[i] % 2] += 1
        return min(arr)
