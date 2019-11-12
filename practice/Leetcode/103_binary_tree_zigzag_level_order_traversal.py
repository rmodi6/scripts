# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        fringe = deque([(root, 0)])

        ans = []
        while len(fringe) > 0:
            node, level = fringe.popleft()
            if len(ans) <= level:
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            if node.left is not None:
                fringe.append((node.left, level + 1))
            if node.right is not None:
                fringe.append((node.right, level + 1))
        
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
            
        return ans
