# https://leetcode.com/contest/weekly-contest-157/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ls = 1
        d = {}
        for i in range(0, len(arr)):
            if arr[i] not in d:
                d[arr[i] + difference] = 1
            else:
                d[arr[i] + difference] = d[arr[i]] + 1
            ls = max(ls, d[arr[i] + difference])
        return ls
