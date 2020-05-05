# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [-1 for i in range(26)]
        for i, c in enumerate(s):
            index = ord(c) - 97
            if arr[index] == -2:
                continue
            if arr[index] == -1:
                arr[index] = i
            else:
                arr[index] = -2
        ans = float('inf')
        for a in arr:
            if a > -1:
                ans = min(ans, a)
        if ans == float('inf'):
            ans = -1
        return ans
