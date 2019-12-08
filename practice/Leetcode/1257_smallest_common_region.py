# https://leetcode.com/contest/biweekly-contest-13/problems/smallest-common-region/

class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        def get_parents(region, hmap):
            node = hmap[region]
            if node.parent is None:
                return [node.val]
            
            return [node.val] + get_parents(node.parent.val, hmap)
        
        hashmap = {}
        for l in regions:
            parent = l[0]
            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            for c in l[1:]:
                hashmap[c] = TreeNode(c, parent=hashmap[parent])
                
        parents1 = get_parents(region1, hashmap)
        parents2 = get_parents(region2, hashmap)
        if len(parents1) > len(parents2):
            parents1 = parents1[(len(parents1) - len(parents2)):]
        elif len(parents2) > len(parents1):
            parents2 = parents2[(len(parents2) - len(parents1)):]
        for i in range(len(parents1)):
            if parents1[i] == parents2[i]:
                return parents1[i]
