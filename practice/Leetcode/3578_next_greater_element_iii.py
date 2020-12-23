# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3578/

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nstr = str(n)
        i = len(nstr) - 2
        j = i + 1
        while i > -1 and nstr[i+1] <= nstr[i]:
            i -= 1
        if i < 0:
            return -1
        while j > -1 and nstr[j] <= nstr[i]:
            j -= 1
        nstr = list(nstr)
        nstr[i], nstr[j] = nstr[j], nstr[i]
        ans = int(''.join(nstr[:i+1] + nstr[:i:-1]))
        return -1 if ans >= 2**31 else ans
