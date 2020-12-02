# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3526/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(A):
            A[i] = [(1-j) for j in row[::-1]]
        return A
