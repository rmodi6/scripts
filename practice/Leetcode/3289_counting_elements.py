# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = {}
        count = 0
        for i in arr:
            hmap[i] = hmap.get(i, [0, True])
            hmap[i][0] += 1
            if hmap.get(i+1, [0, False])[1]:
                count += 1
                hmap[i][0] -= 1
                # hmap[i][1] = True
            if hmap.get(i-1, [0, False])[0] > 0:
                count += hmap.get(i-1)[0]
                hmap[i-1][0] = 0
        return count
