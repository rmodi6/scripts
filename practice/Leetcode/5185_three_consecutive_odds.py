# https://leetcode.com/contest/weekly-contest-202/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for n in arr:
            if n % 2 == 1:
                oddCount += 1
                if oddCount == 3:
                    return True
            else:
                oddCount = 0
        return False
