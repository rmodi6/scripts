# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3372/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        def subSum(node, parentSum):
            currSum = parentSum + node.val
            if node.left is None and node.right is None:
                return currSum
            leftSum = rightSum = 0
            if node.left is not None:
                leftSum = subSum(node.left, currSum * 10)
            if node.right is not None:
                rightSum = subSum(node.right, currSum * 10)
            return leftSum + rightSum
    
        return subSum(root, 0)
