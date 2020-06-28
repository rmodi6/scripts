# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3374/

from collections import defaultdict
import bisect

class Solution:
    def travel(self, _itinerary, _hmap):
        if len(_itinerary) == self.n:
            return _itinerary 
        origin = _itinerary[-1]
        for i, nextDest in enumerate(_hmap[origin]):
            if not self.visited[origin][i]:
                self.visited[origin][i] = True
                ans = self.travel(_itinerary + [nextDest], _hmap)
                self.visited[origin][i] = False
                if ans:
                    return ans
        return False
        
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:   
        self.n = len(tickets) + 1
        hmap = defaultdict(list)
        for f, t in tickets:
            bisect.insort(hmap[f], t)
        self.visited = {}
        for f, li in hmap.items():
            self.visited[f] = [False for _ in li]
        itinerary = ['JFK']
        return self.travel(itinerary, hmap)
