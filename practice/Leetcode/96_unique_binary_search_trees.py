# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0: 1, 1: 1}
        
        def helper(x):
            if x in dp:
                return dp[x]
            ans = 0
            for i in range(1, x+1):
                ans += helper(i-1)*helper(x-i)
            dp[x] = ans
            return ans
            
        return helper(n)