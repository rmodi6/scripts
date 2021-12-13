# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n%2 else []
        for i in range(1, n//2+1):
            ans += [i, -i]
        return ans
