# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        hashmap = {}
        
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            hashmap[root.val] = hashmap.get(root.val, 0) + 1
            inorder(root.right)
            
        inorder(root)
            
        max_count = max(hashmap.values())
        
        ans = []
        for key, count in hashmap.items():
            if count == max_count:
                ans.append(key)
                
        return ans
