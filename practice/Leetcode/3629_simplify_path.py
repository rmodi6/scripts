# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/

class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split('/'):
            if p == '.' or p == '':
                continue
            elif p == '..':
                ans = ans[:-1] if len(ans) > 0 else ans
            else:
                ans.append(p)
        return '/' + '/'.join(ans)
