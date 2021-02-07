# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        indices = [i for i, ch in enumerate(s) if c == ch]
        p, q = 0, 1
        i = 0
        while len(ans) < len(s):
            if q < len(indices):
                d1, d2 = abs(i - indices[p]), abs(i - indices[q])
                if d2 <= d1:
                    p += 1
                    q += 1
            else:
                d1 = d2 = abs(i - indices[p])
            ans.append(min(d1, d2))
            i += 1
        return ans
