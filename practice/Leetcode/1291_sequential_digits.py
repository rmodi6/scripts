# https://leetcode.com/contest/weekly-contest-167/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_low = str(low)
        l = len(str_low)
        ans = []
        fd = int(str_low[0])
        while l <= len(str(high)):
            while fd + l - 1 < 10:
                n = str(fd)
                for i in range(fd+1, fd+l):
                    n += str(i)
                if int(n) >= low and int(n) <= high:
                    ans.append(int(n))
                fd += 1
            fd = 1
            l += 1
        return ans
