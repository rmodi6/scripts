# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isBST(root, max_val, min_val):
            if root is None:
                return True
            if root.val < max_val and root.val > min_val:
                return isBST(root.left, min(max_val, root.val), min_val) and isBST(root.right, max_val, max(min_val, root.val))
            return False
        
        return isBST(root, float('inf'), -float('inf'))
