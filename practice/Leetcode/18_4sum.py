# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def ksum(k, ind, indices, nums, target):
            ans = []
            if k == 2:
                hmap = {}
                for i in range(ind + 1, len(nums)):
                    n = nums[i]
                    if i not in indices:
                        if n in hmap:
                            n2 = hmap[n]
                            l = [n, n2]
                            for index in indices:
                                l.append(nums[index])
                            ans.append(sorted(l))
                        hmap[target - n] = n
            else:                               
                for i in range(ind + 1, len(nums)):
                    n = nums[i]
                    if i not in indices:
                        indices.add(i)
                        ans.extend(ksum(k - 1, i, indices, nums, target - n))
                        indices.remove(i)
            return ans
        ans = ksum(4, -1, set(), nums, target)
        uniq_ans = []
        hset = set()
        for a in ans:
            ta = tuple(a)
            if ta not in hset:
                hset.add(ta)
                uniq_ans.append(a)
        return uniq_ans
