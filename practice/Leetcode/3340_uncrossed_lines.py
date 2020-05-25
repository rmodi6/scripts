# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(B))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if A[i] == B[j] else 0
                elif i == 0:
                    dp[i][j] = max(dp[i][j-1], 1 if A[i] == B[j] else 0)
                elif j == 0:
                    dp[i][j] = max(dp[i-1][j], 1 if A[i] == B[j] else 0)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (1 if A[i] == B[j] else 0))
        return dp[-1][-1]