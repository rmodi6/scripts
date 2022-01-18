# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        hmap = {}
        wordSet = set()
        i = 0
        while i < len(pattern):
            ch, word = pattern[i], words[i]
            if ch in hmap:
                if hmap[ch] != word:
                    return False
            elif word in wordSet:
                return False
            hmap[ch] = word
            wordSet.add(word)
            i += 1
        return True
