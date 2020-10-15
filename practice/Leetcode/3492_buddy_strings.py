# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        cnt = []
        for i in range(len(A)):
            if A[i] != B[i]:
                cnt.append(i)
        if len(cnt) == 2:
            return A[cnt[0]] == B[cnt[1]] and A[cnt[1]] == B[cnt[0]]
        if len(cnt) == 0:
            return len(A) != len(set(A))
