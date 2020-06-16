# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3361/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def binary_search(node, val):
            if node is None:
                return None
            if node.val == val:
                return node
            if node.val < val:
                return binary_search(node.right, val)
            return binary_search(node.left, val)
        
        return binary_search(root, val)
