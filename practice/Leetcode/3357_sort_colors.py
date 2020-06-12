# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.append(-1)
        i = 0
        while nums[i] != -1:
            if nums[i] == 0:
                del nums[i]
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                nums.append(2)
                del nums[i]
            else:
                i += 1
        nums.remove(-1)
