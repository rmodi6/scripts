# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(len(word1)):
            for j in range(len(word2)):
                curr_distance = int(word1[i] != word2[j])
                dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j] + curr_distance)
        return dp[-1][-1]
