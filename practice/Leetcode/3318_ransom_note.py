# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        magazine_dict = {}
        for c in ransomNote:
            ransom[c] = ransom.get(c, 0) + 1
        for c in magazine:
            magazine_dict[c] = magazine_dict.get(c, 0) + 1
        for c in ransom:
            if ransom[c] > magazine_dict.get(c, 0):
                return False
        return True
