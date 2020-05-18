# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s2map, s1map = Counter(s2[:len(s1)]), Counter(s1)
        if s2map == s1map:
            return True
        for i in range(len(s1), len(s2)):
            s2map[s2[i]] += 1
            if s2map[s2[i-len(s1)]] == 1:
                del s2map[s2[i-len(s1)]]
            else:
                s2map[s2[i-len(s1)]] -= 1
            if s2map == s1map:
                return True
        return False
