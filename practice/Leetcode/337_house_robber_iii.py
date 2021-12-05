# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.robUtil(root))
    
    def robUtil(self, node):
        if not node:
            return [0, 0]
        l1, l2 = self.robUtil(node.left)
        r1, r2 = self.robUtil(node.right)
        n1 = node.val + l2 + r2
        n2 = max(l1 + r1, l1 + r2, l2 + r1, l2 + r2)
        return [n1, n2]
