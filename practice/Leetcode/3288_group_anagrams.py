# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        return anagrams.values()
