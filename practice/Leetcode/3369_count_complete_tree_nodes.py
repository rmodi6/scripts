# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3369/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
