# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda i: sum(mat[i]))[:k]
