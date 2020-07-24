# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3400/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path)
                return 
            for child in graph[node]:
                dfs(child, path + [child])
            
        dfs(0, [0])
        return ans
