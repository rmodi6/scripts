# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def traverse(node, x, y, heap):
            if node:
                heapq.heappush(heap, (x, y, node.val))
                traverse(node.left, x-1, y+1, heap)
                traverse(node.right, x+1, y+1, heap)
                
        heap = []
        traverse(root, 0, 0, heap)
        ans, px = [], None
        while heap:
            x, y, val = heapq.heappop(heap)
            if x == px:
                ans[-1].append(val)
            else:
                px = x
                ans.append([val])
        return ans
