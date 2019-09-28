# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer, right_pointer, max_area = 0, len(height) - 1, 0
        while left_pointer < right_pointer:
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area
        