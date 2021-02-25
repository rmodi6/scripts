# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        ans = 0
        if nums != sorted_nums:
            i, j = 0, len(nums)-1
            while nums[i] == sorted_nums[i]:
                i += 1
            while nums[j] == sorted_nums[j]:
                j -= 1
            ans = j - i + 1
        return ans
