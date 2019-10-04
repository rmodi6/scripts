# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ''
        replacements = {}
        for i, index in enumerate(indexes):
            source = sources[i]
            if S[index:index + len(source)] == source:
                replacements[index] = (len(source), targets[i])
        i = 0
        while i < len(S):
            s = S[i]
            if i not in replacements:
                ans += s
                i += 1
            else:
                ans += replacements[i][1]
                i += replacements[i][0]            
        return ans
        