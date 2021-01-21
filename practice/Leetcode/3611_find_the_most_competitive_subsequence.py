# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(nums) - i > k - len(stack):
                stack.pop()
            stack.append(n)
        return stack[:k]
