# https://leetcode.com/contest/biweekly-contest-32/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        for n in arr:
            while n != i:
                if k == 1:
                    return i
                i += 1
                k -= 1
            i += 1
        return i + k - 1
