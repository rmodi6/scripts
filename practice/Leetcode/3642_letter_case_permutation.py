# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for ch in S.lower()[::-1]:
            if ch.isalpha():
                ans = [ch + a for a in ans] + [ch.upper() + a for a in ans]
            else:
                ans = [ch + a for a in ans]
        return ans
