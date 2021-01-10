# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/

from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9+7
        nums = SortedList()
        counter = {}
        cost = 0
        for i in instructions:
            if not nums:
                nums.add(i)
                counter[i] = counter.get(i, 0) + 1
            else:
                if i <= nums[0] or i >= nums[-1]:
                    pass
                else:
                    left = nums.bisect_left(i)
                    right = len(nums) - left - counter.get(i, 0)
                    cost = (cost + min(left, right)) % mod
                nums.add(i)
                counter[i] = counter.get(i, 0) + 1
        return cost
