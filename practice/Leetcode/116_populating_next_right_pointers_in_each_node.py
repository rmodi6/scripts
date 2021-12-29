# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        root.next = None
        self.connectUtil(root)
        return root
        
    def connectUtil(self, node):
        if node.left:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            else:
                node.right.next = None
            self.connectUtil(node.left)
            self.connectUtil(node.right)
