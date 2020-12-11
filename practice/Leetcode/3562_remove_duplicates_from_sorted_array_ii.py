# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = cnt = 0
        prev = None
        for n in nums:
            if n == prev:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                nums[p] = n
                p += 1
            prev = n
        return p
