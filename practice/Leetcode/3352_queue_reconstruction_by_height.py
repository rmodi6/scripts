# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:              
        ans = []
        height_sorted = sorted(people, key=lambda k: (k[0], -k[1]), reverse=True)
        for p in height_sorted:
            ans.insert(p[1], p)
        return ans
