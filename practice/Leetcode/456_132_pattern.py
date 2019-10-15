# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dp = []
        minimum = None
        maximum = None
        for i, n in enumerate(nums):
            if minimum is None or n <= minimum:
                minimum = n
                dp.append(n)
                continue
            if maximum is None or n >= maximum:
                maximum = n
                dp.append(minimum)
                continue
            j = i - 1
            while j >= 0 and n > dp[j]:
                if n < nums[j]:
                    return True
                j -= 1
            dp.append(minimum)
        return False
