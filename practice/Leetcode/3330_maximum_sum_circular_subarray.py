# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

import numpy as np

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if np.all(np.array(A) < 0):
            return max(A)
        k = self.kadane(A)
        max_sum = sum(A)
        A = [-i for i in A]
        k_inverse = max_sum + self.kadane(A)
        return max(k, k_inverse)
                    
    def kadane(self, arr):
        sum = 0
        maxSum = float('-inf')
        for a in arr:
            sum = max(sum + a, a)
            maxSum = max(maxSum, sum)
        return maxSum
