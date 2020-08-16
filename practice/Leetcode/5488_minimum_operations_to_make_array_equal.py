# https://leetcode.com/contest/weekly-contest-202/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        x = n // 2
        return x * (x + n % 2)
