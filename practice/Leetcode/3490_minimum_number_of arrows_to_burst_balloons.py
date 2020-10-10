# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3490/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        points = sorted(points, key=lambda k: k[1])
        ans = 1
        arrow = points[0][1]
        for point in points:
            if point[0] <= arrow:
                continue
            else:
                ans += 1
                arrow = point[1]
        return ans
