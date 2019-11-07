# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_dp = [0] * len(height)
        for i in range(len(height)):
            if i != 0:
                max_left_dp[i] = max(max_left_dp[i-1], height[i-1])
        max_right_dp = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i != len(height) - 1:
                max_right_dp[i] = max(max_right_dp[i+1], height[i+1])
        ans = 0
        for i in range(len(height)):
            ans += max(min(max_left_dp[i], max_right_dp[i]) - height[i], 0)
        return ans
