# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.deleteNodeUtil(root, key)
        return root
    
    def deleteNodeUtil(self, node, key):
        if not node:
            return None
        elif node.val > key:
            node.left = self.deleteNodeUtil(node.left, key)
        elif node.val < key:
            node.right = self.deleteNodeUtil(node.right, key)
        elif node.val == key:
            if node.left:
                prev = node
                p = node.left
                while p.right:
                    prev = p
                    p = p.right
                node.val, p.val = p.val, node.val
                if prev == node:
                    prev.left = self.deleteNodeUtil(p, key)
                else:
                    prev.right = self.deleteNodeUtil(p, key)
            elif node.right:
                prev = node
                p = node.right
                while p.left:
                    prev = p
                    p = p.left
                node.val, p.val = p.val, node.val
                if prev == node:
                    prev.right = self.deleteNodeUtil(p, key)
                else:
                    prev.left = self.deleteNodeUtil(p, key)                
            else:
                return None
        return node
