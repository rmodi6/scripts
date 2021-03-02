# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = set(range(1, len(nums) + 1))
        present = set()
        ans = []
        for n in nums:
            if n in present:
                ans.append(n)
            else:
                missing.remove(n)
            present.add(n)
        ans.append(next(iter(missing)))
        return ans
