# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        for n in arr:
            while n != i:
                if k == 1:
                    return i
                i += 1
                k -= 1
            i += 1
        return i + k - 1
