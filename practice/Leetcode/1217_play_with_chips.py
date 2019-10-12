# https://leetcode.com/contest/weekly-contest-157/problems/play-with-chips/

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        d = {0: 0, 1: 0}
        for c in chips:
            d[c % 2] += 1
        return min(d.values())