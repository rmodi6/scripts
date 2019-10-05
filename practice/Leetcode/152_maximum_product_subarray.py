# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1, 1]
        max_prod = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                prod = num
                if prod < 0:
                    dp[0] = 1
                    dp[1] = prod
                else:
                    dp[0] = prod
                    dp[1] = 1
            else:
                pos_prod = num * dp[0]
                neg_prod = num * dp[1]
                dp[0] = max(1, pos_prod, neg_prod)
                if min(pos_prod, neg_prod) < 0:
                    dp[1] = min(pos_prod, neg_prod)
                else:
                    dp[1] = 1
                max_prod = max(max_prod, pos_prod, neg_prod)
        return max_prod
