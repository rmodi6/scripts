# https://leetcode.com/contest/biweekly-contest-26/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if node is None:
                return 0
            goodNodes = 0
            if node.val >= maxVal:
                maxVal = node.val
                goodNodes += 1
            goodNodes += dfs(node.left, maxVal)
            goodNodes += dfs(node.right, maxVal)
            return goodNodes
        
        return dfs(root, float('-inf'))
