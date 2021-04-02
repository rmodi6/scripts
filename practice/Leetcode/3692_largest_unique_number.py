# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3692/

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = Counter(A)
        A = sorted(A, key=lambda a: (c[a], -a))
        return A[0] if len(A) > 0 and c[A[0]] == 1 else -1
