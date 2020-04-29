# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3314/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    maxSum = -2147483648
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.recursion(root)
        return self.maxSum
    
    def recursion(self, node):
        if node is None:
            return 0
        left = self.recursion(node.left)
        right = self.recursion(node.right)
        maxPath = max(left + node.val, right + node.val, node.val)
        self.maxSum = max(self.maxSum, maxPath, left + right + node.val, node.val)
        return maxPath
