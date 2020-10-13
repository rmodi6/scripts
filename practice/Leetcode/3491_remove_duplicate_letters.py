# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3491/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        hset = set()
        
        ans = []
        for ch in s:
            freq[ch] -= 1
            
            if ch in hset:
                continue
            
            while ans and ans[-1] > ch and freq[ans[-1]] > 0:
                hset.remove(ans.pop())
            
            ans.append(ch)
            hset.add(ch)
        
        return ''.join(ans)
