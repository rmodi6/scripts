# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [float('inf'), float('inf')]
        for n in nums:
            if n > arr[1]:
                return True
            if n > arr[0]:
                arr[1] = min(arr[1], n)
            arr[0] = min(arr[0], n)
        return False
