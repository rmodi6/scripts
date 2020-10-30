# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        ans.append(str(nums[0]))
        prev = nums[0]
        start = nums[0]
        for n in nums[1:]:
            if n != prev + 1:
                if prev != start:
                    ans[-1] = ans[-1] + '->' + str(prev)
                ans.append(str(n))
                start = n
            prev = n
        if prev != start:
            ans[-1] = ans[-1] + '->' + str(prev)
        return ans
