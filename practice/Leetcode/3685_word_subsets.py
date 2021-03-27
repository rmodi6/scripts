# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3685/

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter = Counter('')
        for b in B:
            b_counts = Counter(b)
            for ch, count in b_counts.items():
                counter[ch] = max(counter.get(ch, 0), count)
        ans = []
        for a in A:
            a_counts = Counter(a)
            s = [a]
            for ch, count in counter.items():
                if count > a_counts.get(ch, 0):
                    s = []
                    break
            ans += s
        return ans
