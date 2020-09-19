# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_low = str(low)
        l = len(str_low)
        ans = []
        fd = int(str_low[0])
        while l <= len(str(high)):
            while fd + l - 1 < 10:
                n = ''.join(str(x) for x in range(fd, fd+l))
                if int(n) >= low and int(n) <= high:
                    ans.append(int(n))
                fd += 1
            fd = 1
            l += 1
        return ans
