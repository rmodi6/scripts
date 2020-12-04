# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, ans):
            if node:
                ans = inorder(node.left, ans)
                ans.right = TreeNode(node.val)
                ans = inorder(node.right, ans.right)
            return ans
        dummy = TreeNode(-1)
        inorder(root, dummy)
        return dummy.right
