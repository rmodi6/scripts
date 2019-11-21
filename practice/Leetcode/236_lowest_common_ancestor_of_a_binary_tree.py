# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        
        def dfs(node, parent):
            if node is None:
                return
            parents[node] = parent
            if p in parents and q in parents:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        
        p_parents = [p]
        curr = parents[p]
        while curr is not None:
            p_parents.append(curr)
            curr = parents[curr]
        
        q_parents = [q]
        curr = parents[q]
        while curr is not None:
            q_parents.append(curr)
            curr = parents[curr]
            
        if len(p_parents) <= len(q_parents):
            q_parents = q_parents[len(q_parents) - len(p_parents):]
        else:
            p_parents = p_parents[len(p_parents) - len(q_parents):]
            
        for i in range(len(p_parents)):
            if p_parents[i] == q_parents[i]:
                return p_parents[i]
            
        return None
