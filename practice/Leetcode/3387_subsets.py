# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        ans = [[]]
        for num in nums:
            ans += [prev + [num] for prev in ans]
        return ans
