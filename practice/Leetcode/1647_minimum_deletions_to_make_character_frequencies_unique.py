# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        buckets = set()
        ans = 0
        for ch, freq in counts.items():
            while freq > 0 and freq in buckets:
                freq -= 1
                ans += 1
            if freq > 0:
                buckets.add(freq)
        return ans
