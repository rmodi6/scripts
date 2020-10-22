# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3500/

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        hset = {}
        hset[A[0]] = [0, 0]
        hset[B[0]] = [0, 0]
        for i in range(len(A)):
            if A[i] not in hset and B[i] not in hset:
                return -1
            if A[i] != B[i]:
                if A[i] in hset:
                    hset[A[i]][1] += 1
                if B[i] in hset:
                    hset[B[i]][0] += 1
            if len(hset.keys()) > 1:
                for e in set(hset.keys()) - set([A[i], B[i]]):
                    del hset[e]
        return min([j for i in hset.values() for j in i])
