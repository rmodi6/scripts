# https://leetcode.com/contest/biweekly-contest-12/problems/tree-diameter/

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = {}
        def make_graph():
            for edge in edges:
                for i in range(2):
                    adj = graph.get(edge[i], [])
                    adj.append(edge[1-i])
                    graph[edge[i]] = adj
        make_graph()
        
        def traverse(v, visited):
            visited.add(v)
            max_length = -1
            max_vertex = None
            flag = True
            for n in graph[v]:
                if n not in visited:
                    flag = False
                    length, end_vertex = traverse(n, visited)
                    if length > max_length:
                        max_length = length
                        max_vertex = end_vertex
            if flag:
                return 0, v
            return max_length + 1, max_vertex
        
        l, v = traverse(edges[0][0], set())
        return traverse(v, set())[0]