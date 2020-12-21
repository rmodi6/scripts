# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3573/

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        ans = A[-1] - A[0]
        for i in range(len(A) - 1):
            max_value = max(A[-1]-K, A[i]+K)
            min_value = min(A[0]+K, A[i+1]-K)
            ans = min(ans, max_value - min_value)
        return ans
