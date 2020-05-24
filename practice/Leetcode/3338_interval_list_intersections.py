# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        p, q = 0, 0
        while p < len(A) and q < len(B):
            if min(A[p][1], B[q][1]) - max(A[p][0], B[q][0]) > -1:
                ans.append([max(A[p][0], B[q][0]), min(A[p][1], B[q][1])])
            if A[p][1] < B[q][1]:
                p += 1
            else:
                q += 1
        return ans
