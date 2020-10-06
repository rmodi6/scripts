# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3485/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root
