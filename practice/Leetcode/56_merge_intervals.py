# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d = {}
        for interval in intervals:
            if interval[0] not in d:
                d[interval[0]] = interval
            else:
                d[interval[0]] = [interval[0], max(d[interval[0]][1], interval[1])]
        merged = []
        for k in sorted(d.keys()):
            interval = d[k]
            if len(merged) > 0 and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged
