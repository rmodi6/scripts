# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3620/

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        hset = {}
        ans = 0
        for row in grid:
            if sum(row) > 1:
                for i, v1 in enumerate(row):
                    if v1:
                        for j, v2 in enumerate(row[i+1:]):
                            if v2:
                                ans += hset.get((i, j), 0)
                                hset[(i, j)] = hset.get((i, j), 0) + 1
        return ans
