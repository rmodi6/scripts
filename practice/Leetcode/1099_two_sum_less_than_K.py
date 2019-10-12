# https://leetcode.com/problems/two-sum-less-than-k/submissions/

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A = sorted(A)
        i = 0
        j = len(A) - 1
        ans = -1
        while i < j:
            S = A[i] + A[j]
            if S < K:
                ans = max(ans, S)
                i += 1
            else:
                j -= 1
        return ans
