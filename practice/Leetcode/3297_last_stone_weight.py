# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in stones:
            heapq.heappush(pq, (-1 * i, i))

        while len(pq) > 1:
            new_stone = abs(heapq.heappop(pq)[1] - heapq.heappop(pq)[1])
            if new_stone > 0:
                heapq.heappush(pq, (-1 * new_stone, new_stone))
        return heapq.heappop(pq)[1] if pq else 0
