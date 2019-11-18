# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return
                else:
                    return helper(node.left)
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return
                else:
                    return helper(node.right)
        
        if root is None:
            return TreeNode(val)
        helper(root)
        return root
