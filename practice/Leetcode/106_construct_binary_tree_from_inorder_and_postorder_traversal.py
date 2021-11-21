# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeUtil(inorder, postorder)
    
    def buildTreeUtil(self, inorder, postorder):
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        if i > 0:
            root.left = self.buildTreeUtil(inorder[:i], postorder[:i])
        if i < len(inorder) - 1:
            root.right = self.buildTreeUtil(inorder[i+1:], postorder[i:-1])
        return root
