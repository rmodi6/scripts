# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        r = p+q+1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[r] = nums1[p]
                p -= 1
            else:
                nums1[r] = nums2[q]
                q -= 1
            r -= 1
        while q >= 0:
            nums1[r] = nums2[q]
            q -= 1
            r -= 1
