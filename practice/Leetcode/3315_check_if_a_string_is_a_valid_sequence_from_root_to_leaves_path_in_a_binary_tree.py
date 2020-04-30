# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.dfs(root, arr, 0)
    
    def dfs(self, node, arr, i):
        if i < len(arr) and (node is None or node.val != arr[i]):
            return False
        if i == len(arr) - 1:
            if (node.left is not None or node.right is not None):
                return False
            else:
                return True
        return self.dfs(node.left, arr, i+1) or self.dfs(node.right, arr, i+1)
