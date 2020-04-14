# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        a = 0
        for e in shift:
            a += e[1] * (-1 if e[0] == 0 else 1)
        ans = list(s)
        for i in range(len(s)):
            new_index = (i + a) % len(s)
            ans[new_index] = s[i]
        return ''.join(ans)
