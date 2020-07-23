# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hset = set()
        [hset.remove(num) if num in hset else hset.add(num) for num in nums]
        return list(hset)
