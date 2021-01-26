# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        best = [[float("inf")] * c for _ in range(r)]
        best[0][0] = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = [(0, 0, 0)]
        dest = (r-1, c-1)
        while q:
            effort, i, k = heapq.heappop(q)
            if (i, k) == dest:
                return effort
            
            for x, y in directions:
                nxt_i, nxt_k = i + x, k + y
                if 0 <= nxt_i < r and 0 <= nxt_k < c:
                    nxt_effort = max(effort, abs(heights[nxt_i][nxt_k] - heights[i][k]))
                    if nxt_effort < best[nxt_i][nxt_k]:
                        best[nxt_i][nxt_k] = nxt_effort
                        heapq.heappush(q, (nxt_effort, nxt_i, nxt_k))
