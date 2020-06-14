# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3360/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        m = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
        for f in flights:
            s, d, c = f
            m[s][d] = c
            
        heap = [] 
        heapq.heappush(heap,(0,src,-1))
        
        while heap:
            c, d, p = heapq.heappop(heap)
            if p > K:
                continue
            if d == dst:
                return c
            
            for j in range(len(m)):
                if j != d and m[d][j] != float('inf'):
                    heapq.heappush(heap, (c+m[d][j], j, p+1))
        
        return -1
