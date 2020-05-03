# https://leetcode.com/contest/weekly-contest-187/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s1, s2 = set(), set()
        for p in paths:
            s1.add(p[0])
            s2.add(p[1])
        return list(s2 - s1)[0]
