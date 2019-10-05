# https://leetcode.com/contest/biweekly-contest-10/problems/two-sum-bsts/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        dp = {}
        
        def findTarget(root1, root2, target):
            if root1 is None or root2 is None:
                return False
            if (root1, root2) in dp:
                return dp[(root1, root2)]
            s = root1.val + root2.val
            result = None
            if s == target:
                return True
            elif s < target:
                result = findTarget(root1.right, root2, target) or findTarget(root1, root2.right, target)
            else:
                result = findTarget(root1.left, root2, target) or findTarget(root1, root2.left, target)    
            dp[(root1, root2)] = result
            return result
        
        
        return findTarget(root1, root2, target)