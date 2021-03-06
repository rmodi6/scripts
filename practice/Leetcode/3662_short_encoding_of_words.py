# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3662/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        def isPart(w1, w2):
            return w1 == w2[-len(w1):]
        
        ans = 0
        words = sorted(words, key=lambda word: len(word))
        for i, word in enumerate(words):
            flag = 1
            for other_word in words[i+1:]:
                if isPart(word, other_word):
                    flag = 0
                    break
            ans += flag * (len(word) + 1)
        return ans
