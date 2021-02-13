# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3624/

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        dists = [(distance(squirrel, nut), distance(tree, nut)) for nut in nuts]
        dists = sorted(dists, key=lambda k: (k[0]-k[1]))
        ans = sum(dists[0])
        for dist in dists[1:]:
            ans += dist[1]*2
        return ans
