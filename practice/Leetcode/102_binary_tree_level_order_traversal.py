# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [(root, 1)]
        ans = []
        while queue:
            node, level = queue[0]
            queue = queue[1:]
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            if len(ans) < level:
                ans.append([node.val])
            else:
                ans[-1].append(node.val)
        return ans
