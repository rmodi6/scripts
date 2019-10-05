# https://leetcode.com/contest/biweekly-contest-10/problems/stepping-numbers

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def findDigits(prev_digits, i):
            if i == 0:
                return [prev_digits]
            step_down = int(str(prev_digits)[-1]) - 1
            step_up = int(str(prev_digits)[-1]) + 1
            l = []
            if len(str(step_down)) == 1:
                l += findDigits(int(str(prev_digits) + str(step_down)), i - 1)
            if len(str(step_up)) == 1:
                l += findDigits(int(str(prev_digits) + str(step_up)), i - 1)
            return l
            
        
        ans = []
        i = len(str(low))
        while i <= len(str(high)):
            for x in range(10):
                if i > 1 and x == 0:
                    continue
                ans += findDigits(x, i - 1)
            i += 1
        res = []
        for a in ans:
            if a < low:
                continue
            if a > high:
                break
            res.append(a)
        return res
