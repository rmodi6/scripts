# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3416/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff, ans = float('inf'), 0
        p = root
        while p:
            if abs(target - p.val) < diff:
                diff = abs(target - p.val)
                ans = p.val
            if target > p.val:
                p = p.right
            else:
                p = p.left
        return ans
