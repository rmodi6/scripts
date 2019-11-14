# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def inorder(node, counter):
            if node is None:
                return None, counter
            
            found, counter = inorder(node.left, counter)
            if found is not None:
                return found, counter
            
            counter += 1
            if counter == k:
                return node.val, counter
            return inorder(node.right, counter)

        return inorder(root, 0)[0]
