# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def solution(n, valid_characters):
            if n == 1:
                return len(valid_characters)
            ans = 0
            for i in range(len(valid_characters)):
                ans += solution(n-1, valid_characters[i:])
            return ans
        
        return solution(n, ["a","e","i","o","u"])
