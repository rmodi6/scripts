# https://leetcode.com/problems/reorganize-string/submissions/

import heapq as hq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freqMap = Counter(s)
        for c, freq in freqMap.items():
            hq.heappush(heap, (-freq, c))
        ans = '0'
        while heap:
            freq, c = hq.heappop(heap)
            if c == ans[-1]:
                if not heap:
                    return ''
                nextFreq, nextC = hq.heappop(heap)
                ans += nextC
                if nextFreq < -1:
                    hq.heappush(heap, (nextFreq+1, nextC))
            ans += c
            if freq < -1:
                hq.heappush(heap, (freq+1, c))
        return ans[1:]
