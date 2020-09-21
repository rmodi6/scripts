# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/

import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 0:
            return True
        heap1, heap2 = [], []
        for trip in trips:
            heapq.heappush(heap1, (trip[1], trip[0]))
            heapq.heappush(heap2, (trip[2], trip[0]))
        total = 0
        dest, num2 = heapq.heappop(heap2)
        while heap1:
            src, num1 = heapq.heappop(heap1)
            while dest <= src:
                total -= num2
                dest, num2 = heapq.heappop(heap2)
            total += num1
            if total > capacity:
                return False
        return True
