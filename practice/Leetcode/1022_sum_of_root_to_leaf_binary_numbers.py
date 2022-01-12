# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.util(root, 0)
    
    def util(self, node, su):
        if not node:
            return 0
        if not node.left and not node.right:
            return 2*su + node.val
        return self.util(node.left, 2*su+node.val) + self.util(node.right, 2*su+node.val)
