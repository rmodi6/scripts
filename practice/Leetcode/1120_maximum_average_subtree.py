# https://leetcode.com/problems/maximum-average-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        dp = {}
        def average(node):
            if not node:
                return 0, 0
            if node in dp:
                return dp[node]
            avg1, n1 = average(node.left)
            avg2, n2 = average(node.right)
            s = avg1 * n1 + avg2 * n2 + node.val
            n = n1 + n2 + 1
            dp[node] = [s/n, n]
            return dp[node]
        
        fringe = deque()
        fringe.append(root)
        max_avg = -float('inf')
        while len(fringe) > 0:
            node = fringe.popleft()
            avg, n = average(node)
            if avg > max_avg:
                max_avg = avg
            if node is not None:
                fringe.append(node.left)
                fringe.append(node.right)
            
        return max_avg
