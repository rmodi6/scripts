# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [i*i for i in nums]
        if nums[-1] <= 0:
            return reversed([i*i for i in nums])
        p = 0
        while nums[p] < 0:
            p += 1
        q = p - 1
        ans = []
        while q >= 0 and p < len(nums):
            if nums[p]**2 < nums[q]**2:
                ans.append(nums[p]**2)
                p += 1
            else:
                ans.append(nums[q]**2)
                q -= 1
        while q >= 0:
            ans.append(nums[q]**2)
            q -= 1
        while p < len(nums):
            ans.append(nums[p]**2)
            p += 1
        return ans
