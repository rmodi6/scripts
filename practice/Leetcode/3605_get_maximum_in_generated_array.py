# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:        
        nums = [0,1]
        for i in range(2, n+1):
            nums.append(nums[i//2])
            if i%2:
                nums[-1] += nums[i//2+1]
        return max(nums[:n+1])
