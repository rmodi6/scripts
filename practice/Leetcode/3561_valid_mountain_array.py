# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True
        flag = False
        prev = -1
        for a in arr:
            if a == prev:
                return False
            if increasing:
                if a < prev:
                    increasing = False
                else:
                    flag = prev != -1
            else:
                if a > prev:
                    return False
            prev = a
        return not increasing and flag
