# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        hash_count = [0, 0]
        while True:
            while i > -1:
                if S[i] == '#':
                    hash_count[0] += 1
                elif hash_count[0] > 0:
                    hash_count[0] -= 1
                else:
                    break
                i -= 1
            while j > -1:
                if T[j] == '#':
                    hash_count[1] += 1
                elif hash_count[1] > 0:
                    hash_count[1] -= 1
                else:
                    break
                j -= 1
            if i == -1 and j == -1:
                return True
            if (i == -1 and j != -1) or (i != -1 and j == -1):
                return False
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
