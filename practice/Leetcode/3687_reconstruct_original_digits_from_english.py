# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3687/

class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        ans = [0] * 10
        hmap = {
                'z': ['zero', 0],
                'w': ['two', 2],
                'u': ['four', 4],
                'x': ['six', 6],
                'one': ['one',1],
                'three': ['three',3],
                'five': ['five', 5],
                'seven': ['seven', 7],
                'eight': ['eight',8],
                'nine': ['nine',9]
               }
        for num, v in hmap.items():
            count = float('inf')
            for n in num:
                count = min(count, c.get(n, 0))
            ans[v[1]] += count
            for ch in v[0]:
                c[ch] -= ans[v[1]]
        ret = ''
        for i, count in enumerate(ans):
            ret += count*str(i)
        return ret
