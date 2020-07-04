# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/

class Solution:
    
    def __init__(self):
        self.dp = [1]
        primes = [2, 3, 5]
        pointers = [0] * 6
        while len(self.dp) < 1690:
            nextUglies = list(map(lambda prime: prime * self.dp[pointers[prime]], primes))
            nextUgly = min(nextUglies)
            for i, prime in enumerate(primes):
                if nextUgly == nextUglies[i]:
                    pointers[prime] += 1
            self.dp.append(nextUgly)
    
    def nthUglyNumber(self, n: int) -> int:
        return self.dp[n-1]
