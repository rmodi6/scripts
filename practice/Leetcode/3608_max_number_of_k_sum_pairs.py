# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = {}
        ans = 0
        for n in nums:
            if hmap.get(k-n, 0) > 0:
                ans += 1
                hmap[k-n] -= 1
            else:
                hmap[n] = hmap.get(n, 0) + 1
        return ans
