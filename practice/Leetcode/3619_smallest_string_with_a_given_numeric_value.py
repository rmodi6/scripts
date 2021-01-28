# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        while n > 1:
            i = max(1, k - (n-1)*26)
            ans.append(chr(i+96))
            n -= 1
            k -= i
        ans.append(chr(k+96))
        return ''.join(ans)
