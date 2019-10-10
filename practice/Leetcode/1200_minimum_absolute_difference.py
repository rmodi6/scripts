# https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = {}
        arr = sorted(arr)
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff not in d:
                d[diff] = []
            d[diff].append([arr[i], arr[i+1]])
        return d[min(d.keys())]