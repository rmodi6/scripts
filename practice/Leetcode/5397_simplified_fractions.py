# https://leetcode.com/contest/biweekly-contest-26/problems/simplified-fractions/

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y): 
            while(y): 
                x, y = y, x % y 
            return x 

        def recursion(n):
            if n == 1:
                return []
            ans = recursion(n-1)
            for i in range(1, n):
                if i == 1 or gcd(i, n) == 1: 
                    ans += [f'{i}/{n}']
            return ans
        
        return recursion(n)
