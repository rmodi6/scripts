# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                ans.append(s[i])
                i += 1
                continue
            j = i + 1
            while s[j].isdigit():
                j += 1
            d = int(s[i:j])
            innerS, i = self.getInnerS(s, j+1)
            ans.append(d * self.decodeString(innerS))
        return ''.join(ans)
    
    def getInnerS(self, s, i):
        count = 1
        innerS = []
        while count > 0:
            if s[i] == '[':
                count += 1
            elif s[i] == ']':
                count -= 1
            innerS.append(s[i])
            i += 1
        return ''.join(innerS[:-1]), i
