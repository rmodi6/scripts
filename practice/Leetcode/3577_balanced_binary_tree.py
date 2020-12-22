# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3577/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return True, 0
            left = check(node.left)
            right = check(node.right)
            return left[0] and right[0] and abs(left[1] - right[1]) < 2, max(left[1], right[1]) + 1
        
        return check(root)[0]
