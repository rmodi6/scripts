# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent = self.dfs(root, None, 0, x)
        y_depth, y_parent = self.dfs(root, None, 0, y)
        return x_parent != y_parent and x_depth == y_depth
        
    def dfs(self, node, parent, depth, n):
        if node is None:
            return None, None
        if node.val == n:
            return depth, parent
        a,b = self.dfs(node.left, node, depth+1, n)
        if a is None:
            a, b = self.dfs(node.right, node, depth+1, n)
        return a, b
