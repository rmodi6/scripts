# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.diameter(root)[1]
    
    def diameter(self, node: TreeNode) -> int:
        if node is None:
            return 0, 0
        depth_left, diam_left = self.diameter(node.left)
        depth_right, diam_right = self.diameter(node.right)
        return max(depth_left, depth_right) + 1, max([depth_left + depth_right, diam_left, diam_right])
