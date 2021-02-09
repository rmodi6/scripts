# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:        
        def dfs(node, cumsum):
            if node:
                cumsum = dfs(node.right, cumsum) + node.val
                node.val = cumsum
                cumsum = dfs(node.left, cumsum)
            return cumsum
        dfs(root, 0)
        return root
