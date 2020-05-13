# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        ans = ''
        for n in num:
            while k > 0 and len(ans) > 0 and ans[-1] > n:
                ans = ans[:-1]
                k -= 1
            ans = ans + n
        if k > 0:
            ans = ans[:-k]
        return str(int(ans)) if len(ans) > 0 else '0'