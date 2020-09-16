# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3462/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        max_xor = 0
        
        for i in reversed(range(L)):
            max_xor <<= 1
            prefixes = {num >> i for num in nums}
            curr_xor = max_xor | 1
            
            for p in prefixes:
                if p ^ curr_xor in prefixes:
                    max_xor |= 1
            
        return max_xor
