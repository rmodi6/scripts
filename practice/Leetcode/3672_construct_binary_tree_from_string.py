# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3672/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def nextDigit(s):
            d = ''
            i = 0
            while i < len(s) and (s[i].isdigit() or s[i] == '-'):
                d += s[i]
                i += 1
            return int(d), s[i:]
        
        def getTree(s):
            if not s:
                return None, ''
            d, s = nextDigit(s)
            left = right = None
            if s and s[0] == '(':
                left, s = getTree(s[1:])
                if s and s[0] == '(':
                    right, s = getTree(s[1:])
            return TreeNode(d, left, right), s[1:]
                
        return getTree(s)[0]
