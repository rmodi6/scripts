# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        hmap = {}
        def dfs(node, level):
            if node:
                hmap[level] = hmap.get(level, []) + [node.val]
                dfs(node.left, level+1)
                dfs(node.right, level+1)
        
        dfs(root, 0)
        return [sum(l)/len(l) for l in hmap.values()]
