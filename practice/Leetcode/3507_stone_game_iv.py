# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3507/

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False, True, False]
        for i in range(3, n+1):
            k = 1
            while i - k**2 >= 0:
                if dp[i-k**2] == False:
                    dp.append(True)
                    break
                k += 1
            else:
                dp.append(False)
        return dp[n]
