# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set('aeiouAEIOU')
        ans = []
        for i, word in enumerate(S.split()):
            newWord = ''
            if word[0] in vowels:
                newWord = word + 'ma'
            else:
                newWord = word[1:] + word[0] + 'ma'
            newWord += ('a' * (i+1))
            ans.append(newWord)
        return ' '.join(ans)
