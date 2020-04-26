# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3311/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2))] for j in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if text1[i] == text2[j] else 0
                elif i == 0:
                    dp[i][j] = max(dp[i][j-1], 1 if text1[i] == text2[j] else 0)
                elif j == 0:
                    dp[i][j] = max(dp[i-1][j], 1 if text1[i] == text2[j] else 0)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (1 if text1[i] == text2[j] else 0))
        return dp[-1][-1]
