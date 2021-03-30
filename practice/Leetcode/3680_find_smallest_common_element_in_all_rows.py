# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3680/

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ans = set(mat[0])
        for row in mat:
            ans = ans.intersection(set(row))
        return min(ans) if len(ans) > 0 else -1
