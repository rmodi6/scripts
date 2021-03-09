# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        def addRow(node, v, d):
            if node:
                if d == 2:
                    left_node = TreeNode(v, left=node.left)
                    right_node = TreeNode(v, right=node.right)
                    node.left = left_node
                    node.right = right_node
                else:
                    addRow(node.left, v, d-1)
                    addRow(node.right, v, d-1)
                
        if not root:
            return root
        if d == 1:
            node = TreeNode(v, root)
            root = node
        else:
            addRow(root, v, d)
        return root
