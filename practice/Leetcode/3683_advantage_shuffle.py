# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3683/

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        b_indices = sorted(range(len(B)), key=lambda k: B[k])
        A = sorted(A)
        i = j = 0
        ans = ['_'] * len(A)
        rem = []
        while j < len(A):
            while j < len(A) and A[j] <= B[b_indices[i]]:
                rem.append(A[j])
                j += 1
            if j < len(A):
                ans[b_indices[i]] = A[j]
                j += 1
            else:
                break
            i += 1
        for i in range(len(ans)):
            if ans[i] == '_':
                ans[i] = rem.pop(0)
        return ans
