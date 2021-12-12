# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total/2
        if target != int(target):
            return False
        return self.subsetSum(nums, int(target))

    def subsetSum(self, arr, target):
        dp = [[False] * (target+1)] * (2)
        for i in range(2):
            dp[i][0] = True
        for i in range(1, len(arr)+1):
            n = arr[i-1]
            for s in range(target, n-1, -1):
                dp[i%2][s] = (dp[1-i%2][s] or dp[1-i%2][s-n])
        return dp[len(arr)%2][target]
