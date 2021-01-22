# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        f1 = [count for word, count in c1.items()]
        f2 = [count for word, count in c2.items()]
        return c1.keys() == c2.keys() and sorted(f1) == sorted(f2)
