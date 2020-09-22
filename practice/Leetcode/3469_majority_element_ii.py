# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3469/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        counts, candidates = [0, 0], [None, None]
        for num in nums:
            if num in candidates:
                counts[candidates.index(num)] += 1
            elif 0 in counts:
                idx = counts.index(0)
                counts[idx] += 1
                candidates[idx] = num
            else:
                counts = [c-1 for c in counts]
        
        ans = []
        for candidate in candidates:
            if nums.count(candidate) > len(nums)//3:
                ans.append(candidate)
        
        return ans
