# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3524/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def tiltSum(node):
            if not node:
                return 0, 0
            lt, ls = tiltSum(node.left)
            rt, rs = tiltSum(node.right)
            return abs(ls - rs) + lt + rt, ls + rs + node.val
        return tiltSum(root)[0]
