# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3460/

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        def inorder_traverse(node):
            if node.left:
                return inorder_traverse(node.left)
            return node
        
        def reverse_inorder(node):
            if not node.parent:
                return None
            if node.parent.left == node:
                return node.parent
            return reverse_inorder(node.parent)
        
        if node.right:
            return inorder_traverse(node.right)
        if node.parent and node.parent.left == node:
            return node.parent
        if not node.parent:
            return None
        return reverse_inorder(node.parent)
