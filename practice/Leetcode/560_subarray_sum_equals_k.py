# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        hmap = defaultdict(lambda: 0)
        hmap[0] = 1
        for n in nums:
            s += n
            ans += hmap[s-k]
            hmap[s] = hmap[s] + 1
        return ans
