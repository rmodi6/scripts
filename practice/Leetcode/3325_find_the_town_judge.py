# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        hmap = {}
        all = set([i for i in range(1, N+1)])
        left = set()
        for t in trust:
            left.add(t[0])
            if t[1] not in hmap:
                hmap[t[1]] = set()
            hmap[t[1]].add(t[0])
        for j in hmap.keys():
            if hmap[j] == all - set([j]) and j not in left:
                return j
        return -1
