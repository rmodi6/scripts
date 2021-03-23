# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        wset = set(wordlist)
        hmap = {}
        for word in wordlist:
            word_lower = word.lower()
            if word_lower not in hmap:
                hmap[word_lower] = word
                for v in vowels:
                    word_lower = word_lower.replace(v, '_')
                if word_lower not in hmap:
                    hmap[word_lower] = word
        ans = []
        for q in queries:
            if q in wset:
                ans.append(q)
            elif q.lower() in hmap:
                ans.append(hmap[q.lower()])
            else:
                q_lower = q.lower()
                for v in vowels:
                    q_lower = q_lower.replace(v, '_')
                ans.append(hmap.get(q_lower, ''))
        return ans
