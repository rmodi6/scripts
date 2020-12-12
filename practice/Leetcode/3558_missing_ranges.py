# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3558/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        p = 0
        i = lower
        while i <= upper and p < len(nums):
            if i == nums[p]:
                p += 1
                i += 1
            elif i < nums[p]:
                j = nums[p] - 1
                if i == j:
                    ans.append(str(i))
                else:
                    ans.append('{}->{}'.format(i, j))
                i = nums[p] + 1
                p += 1
        if i < upper:
            ans.append('{}->{}'.format(i, upper))
        elif i == upper:
            ans.append(str(i))
        return ans