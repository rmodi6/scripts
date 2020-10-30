# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3512/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if sum(seats) == 1:
            return max(seats.index(1), len(seats)-1-seats.index(1))
        if sum(seats) >= len(seats) - 2:
            return 1
        ans = 1
        i = 0
        start = -1
        while i < len(seats):
            if seats[i] == 1:
                if start == -1:
                    dist = i - 0
                else:
                    dist = (i - start)//2
                ans = max(ans, dist)
                start = i
            i += 1
        return max(ans, (i - start - 1))
