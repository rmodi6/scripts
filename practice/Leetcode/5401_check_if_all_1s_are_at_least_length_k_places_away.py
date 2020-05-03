# https://leetcode.com/contest/weekly-contest-187/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = k
        for n in nums:
            if n == 1:
                if c < k:
                    return False
                else:
                    c = 0
            else:
                c += 1
        return True
