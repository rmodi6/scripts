# https://leetcode.com/contest/weekly-contest-157/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowelMap = {
            0: [1],
            1: [0, 2],
            2: [0, 1, 3, 4],
            3: [2, 4],
            4: [0]
        }

        dp = [[0 for j in range(5)] for i in range(n + 1)]

        for i in range(5):
            dp[1][i] = 1

        # print(dp)

        mod = 10**9 + 7

        for i in range(1, n):
            for vowel in vowelMap:
                nextVowels = vowelMap[vowel]
                for nextVowel in nextVowels:
                    # print(i, vowel, nextVowel)
                    dp[i+1][nextVowel] = (dp[i+1][nextVowel] + dp[i][vowel]) % mod

        res = 0
        for i in range(5):
            res = (res + dp[n][i]) % mod

        return res
