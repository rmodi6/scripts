# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/

class Solution:
    def countArrangement(self, n: int) -> int:    
        def solution(n, pos, visited):
            count = 0
            if pos > n:
                count += 1
            for i in range(1, n+1):
                if not visited.get(i, False) and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    count += solution(n, pos + 1, visited)
                    visited[i] = False
            return count
                    
        visited = {}
        return solution(n, 1, visited)
