# https://leetcode.com/contest/biweekly-contest-32/problems/can-convert-string-in-k-moves/

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        visited = {}
        for i in range(1, 27):
            visited[i] = i
        for i in range(len(s)):
            si, ti = s[i], t[i]
            diff = ord(ti) - ord(si)
            if diff < 0:
                diff = 26 + diff
            if diff == 0:
                continue
            if visited[diff] <= k:
                visited[diff] += 26
            else:
                return False
        return True
