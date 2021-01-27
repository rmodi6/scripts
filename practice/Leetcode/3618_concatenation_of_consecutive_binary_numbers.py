# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ''
        for i in range(n+1):
            ans += bin(i)[2:]
        return int(ans, 2) % (10**9 + 7)
