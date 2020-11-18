# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3525/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def recursion(node):
            if not node.left and not node.right:
                return node.val, node.val, 0
            if not node.right:
                lmin, lmax, ans = recursion(node.left)
                return min(lmin, node.val), max(lmax, node.val), max(ans, abs(node.val-lmin), abs(node.val-lmax))
            if not node.left:
                rmin, rmax, ans = recursion(node.right)
                return min(rmin, node.val), max(rmax, node.val), max(ans, abs(node.val-rmin), abs(node.val-rmax))
            lmin, lmax, lans = recursion(node.left)
            rmin, rmax, rans = recursion(node.right)
            return min(lmin, rmin, node.val), max(lmax, rmax, node.val), max(lans, rans, abs(node.val-min(lmin, rmin)), abs(node.val-max(lmax, rmax)))
        
        return recursion(root)[-1]
