# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices = []
        ans = ''
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, len(ans)))
                ans += c
            elif c == ')':
                if len(stack) > 0:
                    stack.pop()
                    ans += c
            else:
                ans += c
        for i in (indices + [idx for (c,idx) in stack])[::-1]:
            ans = ans[:i] + ans[i+1:]
        return ans
