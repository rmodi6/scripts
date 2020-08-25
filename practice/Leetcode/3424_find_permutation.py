# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3424/

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        def recursion(arr, leftIndex, n):
            index = s.find('I', leftIndex)
            i = index if index >= 0 else len(ans) - 1 
            while i >= leftIndex:
                ans[i] = n
                i -= 1
                n += 1
            return index + 1, n
        
        ans = [0] * (len(s) + 1)
        n = 1
        l = 0
        while n < len(ans):
            l, n = recursion(ans, l, n)
        if ans[-1] == 0:
            ans[-1] = n
        return ans
