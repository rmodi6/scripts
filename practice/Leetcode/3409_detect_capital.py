# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or (word[0] == word[0].upper() and word[1:] == word[1:].lower())
